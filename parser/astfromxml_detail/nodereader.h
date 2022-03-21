/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

#pragma once

#include <initializer_list>
#include <type_traits>

#include <QList>

#include "ast.h"
#include "fromxml_fwd.h"

using namespace Python;

using StringList = std::initializer_list<const char*>;
template<int Attr> using AttributeTag = std::integral_constant<int, Attr>;
template<int Child> using ChildTag = std::integral_constant<int, Child>;

enum global_attributes {
    col_offset = -1, lineno = -2,
    end_col_offset = -3, end_lineno = -4,
    last_global_attribute = end_lineno
};
StringList constexpr global_attribute_names = {
    "col_offset", "lineno",
    "end_col_offset", "end_lineno",
};
static_assert(global_attribute_names.size() == -last_global_attribute);

template<typename Attributes, int AttributeCount, typename Children, int ChildCount, typename Reader>
struct NodeReadHelper {
    constexpr NodeReadHelper(Reader* r, StringList attributeNames, StringList childNames)
    : r(r)
    , attributeNames(attributeNames)
    , childNames(childNames)
    {
    }

    template<int N>
    void tryReadAttributes(QStringRef const& attributeName, QStringRef const& attributeValue) {
        if constexpr (N >= 0) {
            if (attributeName == *(r->AttributeNames.begin() + N)) {
                r->readAttribute(AttributeTag<N>{}, attributeValue);
                return;
            }
        }
        else {
            if (attributeName == *(global_attribute_names.begin() - (N+1))) {
                r->readGlobalAttribute(AttributeTag<N>{}, attributeValue);
                return;
            }
        }

        if constexpr (N > last_global_attribute)
            tryReadAttributes<N-1>(attributeName, attributeValue);
        if constexpr (N == last_global_attribute)
            qWarning() << "failed to match xml attribute name:" << attributeName;
    }

    void readAttributes(Stream& s) {
        auto const& attributes = s.attributes();
        for (auto const& attr: attributes) {
            tryReadAttributes<AttributeCount - 1>(attr.name(), attr.value());
        }
    }

    template<int N>
    void readSingleChild(QStringRef const& childName, Stream& s) {
        auto const nameMatches = childName == *(r->ChildNames.begin() + N);
        if (nameMatches) {
            r->readChild(ChildTag<N>{}, s);
        }
        else {
            if constexpr (N > 0)
                readSingleChild<N-1>(childName, s);
            if constexpr (N == 0)
                qWarning() << "failed to match xml child attribute:" << childName;
        }
    }

    void readChildren(Stream& s) {
        if constexpr (ChildCount > 0) {
            auto const name = s.name();
            while (s.readNextStartElement()) {
                auto childName = s.name();
                readSingleChild<ChildCount - 1>(s.name(), s);
            }
        }
        else {
            s.readNextStartElement();
        }
    };

    Reader* r;
    const StringList attributeNames, childNames;
};

template<typename Derived>
void doReadNode(Derived* r, Stream& s)
{
    using ThisReader = NodeReadHelper<
        typename Derived::Attributes, Derived::AttributeNames.size(),
        typename Derived::Children, Derived::ChildNames.size(),
        Derived
    >;

    auto const name = s.name();
    ThisReader reader(r, r->AttributeNames, r->ChildNames);
    reader.readAttributes(s);
    reader.readChildren(s);
}

template<typename AstT>
struct NodeReader
{
    NodeReader(Ast*) {}
    Ast* read(Stream&) { return nullptr; }
};

template<typename AstT>
struct BaseNodeReader
{
    using Children = enum {};
    using Attributes = enum {};

    static constexpr StringList ChildNames = {};
    static constexpr StringList AttributeNames = {};

    BaseNodeReader(Ast* parent) {
        result = new AstT(parent);
    }

    AstT* read(Stream& s) {
        using Derived = NodeReader<AstT>;
        auto* derivedInstance = static_cast<Derived*>(this);
        doReadNode<Derived>(derivedInstance, s);
        return derivedInstance->result;
    }

    void readGlobalAttribute(AttributeTag<col_offset>, QStringRef const& value) {
        result->startCol = value.toInt();
    }

    void readGlobalAttribute(AttributeTag<lineno>, QStringRef const& value) {
        // minus one because our lines are zero-indexed
        result->startLine = value.toInt() - 1;
    }

    void readGlobalAttribute(AttributeTag<end_col_offset>, QStringRef const& value) {
        // minus one because our ranges are [a:b] but Python's are [a:b)
        result->endCol = value.toInt() - 1;
    }

    void readGlobalAttribute(AttributeTag<end_lineno>, QStringRef const& value) {
        // minus one because our lines are zero-indexed
        result->endLine = value.toInt() - 1;
    }

    AstT* result;
};

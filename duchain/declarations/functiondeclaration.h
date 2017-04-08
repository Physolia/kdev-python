/**
    This file is part of KDevelop
    Copyright (C) 2011 Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/


#ifndef PYTHONFUNCTIONDECLARATION_H
#define PYTHONFUNCTIONDECLARATION_H

#include <language/duchain/functiondeclaration.h>
#include <serialization/indexedstring.h>

#include "pythonduchainexport.h"

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT FunctionDeclarationData : public KDevelop::FunctionDeclarationData
{
public:
    FunctionDeclarationData()
        : KDevelop::FunctionDeclarationData()
        , m_isStatic(false)
        , m_isClassMethod(false)
        , m_isProperty(false)
        , m_vararg(-1)
        , m_kwarg(-1) {}

    FunctionDeclarationData(const FunctionDeclarationData& rhs)
        : KDevelop::FunctionDeclarationData(rhs)
        , m_isStatic(rhs.m_isStatic)
        , m_isClassMethod(rhs.m_isClassMethod)
        , m_isProperty(rhs.m_isProperty)
        , m_vararg(rhs.m_vararg)
        , m_kwarg(rhs.m_kwarg) {}

    ~FunctionDeclarationData() {}

    bool m_isStatic: 1;
    bool m_isClassMethod: 1;
    bool m_isProperty: 1; //TODO real property declarations
    short m_vararg;
    short m_kwarg;
};

class KDEVPYTHONDUCHAIN_EXPORT FunctionDeclaration : public KDevelop::FunctionDeclaration
{
public:
    FunctionDeclaration(const FunctionDeclaration &rhs);
    FunctionDeclaration(const KDevelop::RangeInRevision &range, KDevelop::DUContext *context);
    FunctionDeclaration(FunctionDeclarationData &data);
    FunctionDeclaration(FunctionDeclarationData &data, const KDevelop::RangeInRevision &range, KDevelop::DUContext *context);
    ~FunctionDeclaration() override;
    
    enum {
        Identity = 126
    };
    
    inline void setVararg(short vararg) {
        d_func_dynamic()->m_vararg = vararg;
    }
    
    inline short vararg() const {
        return d_func()->m_vararg;
    }
    
    inline void setKwarg(short kwarg) {
        d_func_dynamic()->m_kwarg = kwarg;
    }
    
    inline short kwarg() const {
        return d_func()->m_kwarg;
    }
    
    inline bool isStatic() const {
        return d_func()->m_isStatic;
    }
    
    inline void setStatic(bool isStatic) {
        d_func_dynamic()->m_isStatic = isStatic;
    }
    inline bool isClassMethod() const {
        return d_func()->m_isClassMethod;
    }

    inline void setClassMethod(bool isClassMethod) {
        d_func_dynamic()->m_isClassMethod = isClassMethod;
    }

    inline bool isProperty() const {
        return d_func()->m_isProperty;
    }

    inline void setProperty(bool isProperty) {
        d_func_dynamic()->m_isProperty = isProperty;
    }

    typedef KDevelop::DUChainPointer<FunctionDeclaration> Ptr;
    
private:
    DUCHAIN_DECLARE_DATA(FunctionDeclaration);
};

typedef KDevelop::DUChainPointer<FunctionDeclaration> FunctionDeclarationPointer;
} // namespace Python

#endif // PYTHONFUNCTIONDECLARATION_H

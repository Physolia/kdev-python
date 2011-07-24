/**
    This file is part of KDevelop
    Copyright (C) 2011 Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/


#ifndef HINTEDTYPE_H
#define HINTEDTYPE_H

#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/use.h>

#include "pythonduchainexport.h"
#include <language/editor/modificationrevision.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/typesystem.h>

using namespace KDevelop;

namespace Python {
    
class KDEVPYTHONDUCHAIN_EXPORT HintedTypeData : public KDevelop::AbstractTypeData
{
public:
    /// Constructor
    HintedTypeData()
        : KDevelop::AbstractTypeData(), m_hintedType(0), m_createdByContext((TopDUContext*) 0), m_modificationRevision()
    {
    }
    /// Copy constructor. \param rhs data to copy
    HintedTypeData( const HintedTypeData& rhs )
        : KDevelop::AbstractTypeData(rhs), m_hintedType(rhs.m_hintedType), m_createdByContext(rhs.m_createdByContext), m_modificationRevision(rhs.m_modificationRevision)
    {
    }
    
    HintedTypeData(const AbstractTypeData& rhs)
        : KDevelop::AbstractTypeData(rhs), m_hintedType(0), m_createdByContext((TopDUContext*) 0), m_modificationRevision()
    {
    };
    
    IndexedType m_hintedType;
    IndexedTopDUContext m_createdByContext;
    ModificationRevision m_modificationRevision;
};


/**
* Describes a type which is a hint, and thus kept between parser passes and only deleted if the context which created it
* goes away or is reparsed (it'll create a new one in case the hint still exists)
**/
class KDEVPYTHONDUCHAIN_EXPORT HintedType : public KDevelop::AbstractType
{
public:
    typedef TypePtr<HintedType> Ptr;
    
    HintedType();
    HintedType(const HintedType& rhs);
    HintedType(AbstractTypeData& data);
    void setCreatedBy(TopDUContext* context, int use);
    virtual AbstractType* clone() const;
    virtual uint hash() const;
    const IndexedType& typeHinted() const;
    virtual void accept0(TypeVisitor* v) const;
    
    virtual bool equals(const AbstractType* rhs) const;
    
    enum {
#warning check identity value (62)
        Identity = 62
    };
    
    typedef HintedTypeData Data;
    typedef KDevelop::AbstractType BaseType;
    
protected:
    TYPE_DECLARE_DATA(HintedType);
};

}

#endif // VARIABLELENGTHCONTAINER_H

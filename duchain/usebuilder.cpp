/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010-2011 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/
#include "usebuilder.h"

#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

#include <KUrl>

#include <language/duchain/declaration.h>
#include <language/duchain/use.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/types/structuretype.h>

#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "ast.h"
#include "expressionvisitor.h"

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

UseBuilder::UseBuilder (PythonEditorIntegrator* editor) : UseBuilderBase()
{
    setEditor(editor);
}

void UseBuilder::visitName(NameAst* node)
{
    QList<Declaration*> declarations;
    QList<Declaration*> localDeclarations;
    QList<Declaration*> importedLocalDeclarations;
    {
        DUChainReadLocker lock(DUChain::lock());
        declarations = currentContext()->topContext()->findDeclarations(identifierForNode(node->identifier), CursorInRevision::invalid());
        localDeclarations = currentContext()->findLocalDeclarations(identifierForNode(node->identifier).last(), editorFindRange(node, node).end);
        importedLocalDeclarations = currentContext()->findDeclarations(identifierForNode(node->identifier).last(), editorFindRange(node, node).end);
    }
    Declaration* declaration;
    if ( localDeclarations.length() ) {
        declaration = localDeclarations.last();
        kDebug() << "Using local declaration";
    }
    else if ( importedLocalDeclarations.length() ) {
        declaration = importedLocalDeclarations.last();
        kDebug() << "Using imported local declaration (i.e., argument)";
    }
    else if ( declarations.length() ) {
        declaration = declarations.last();
        kDebug() << "Using global declaration";
    }
    else declaration = 0;
//     kDebug() << currentContext()->type() << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
    
    Q_ASSERT(node->identifier);
    Q_ASSERT(node->hasUsefulRangeInformation); // TODO remove this!
    RangeInRevision useRange(node->identifier->startLine, node->identifier->startCol, node->identifier->endLine, node->identifier->endCol + 1);
    
    if ( declaration && declaration->range() == useRange ) return;
    
    /// debug
    kDebug() << " Registering use for " << node->identifier->value << " at " << useRange.castToSimpleRange() << "with dec" << declaration;
    {
        DUChainReadLocker lock(DUChain::lock());
        Q_ASSERT( ! declaration || declaration->alwaysForceDirect() );
    }
    /// end debug
    UseBuilderBase::newUse(node, useRange, DeclarationPointer(declaration));
}


void UseBuilder::visitAttribute(AttributeAst* node)
{
    ExpressionVisitor v(currentContext(), editor());
    kDebug() << "VisitAttribute start";
    UseBuilderBase::visitAttribute(node);
    kDebug() << "Visit Attribute base end";
    
    v.visitNode(node);
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol, node->attribute->endLine, node->attribute->endCol + 1);
    
    DeclarationPointer declaration = v.lastDeclaration();
    if ( declaration && declaration->range() == useRange ) return;
    /// debug
    if ( declaration ) {
        DUChainReadLocker lock(DUChain::lock());
        kDebug() << "Registering new use for item: " << declaration->toString() << "; Ranges are " << declaration->range().castToSimpleRange() << useRange.castToSimpleRange();
        Q_ASSERT( ! declaration || declaration->alwaysForceDirect() );
    }
    /// end debug
    UseBuilderBase::newUse(node, useRange, declaration);
}


ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}

}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on

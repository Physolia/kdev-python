/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

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
*/


#include "variablecontroller.h"
#include "variable.h"
#include "debugsession.h"
#include <language/duchain/duchainlock.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <interfaces/ilanguagecontroller.h>

#include <debugger/variable/variablecollection.h>
#include <interfaces/icore.h>
#include <QStack>
#include <KMessageBox>
#include <KLocalizedString>
#include <X11/X.h>

using namespace KDevelop;

namespace Python {

VariableController::VariableController(IDebugSession* parent) : IVariableController(parent)
{

}

void VariableController::addWatch(KDevelop::Variable* variable)
{
    kWarning() << "addWatch requested (not implemented)";
}

void VariableController::addWatchpoint(KDevelop::Variable* variable)
{
    kWarning() << "addWatchpoint requested (not implemented)";
}

KDevelop::Variable* VariableController::createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display)
{
    return new Variable(model, parent, expression, display);
}

QString VariableController::expressionUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor)
{
    QString line = doc->line(cursor.line());
    int index = cursor.column();
    QChar c = line[index];
    if ( ! c.isLetterOrNumber() && c != '_' ) {
        return QString();
    }

    int end = index;
    for (; end < line.size(); ++end)
    {
        QChar c = line[end];
        if ( ! ( c.isLetterOrNumber() || c == '_' ) ) {
            break;
        }
    }
    int start = index;
    QStringList openingBrackets = QStringList() << "(" << "[" << "{" << "\"" << "'";
    QStringList closingBrackets = QStringList() << ")" << "]" << "}" << "\"" << "'";
    QStringList sliceChars = QStringList() << "." << "(" << "["; // chars which are allowed to be preceded by a space
    QStack<QString> brackets;
    bool lastWasSlice = false;
    while ( start > 0 ) {
        QChar c = line[start];
        int bracket = closingBrackets.indexOf(c);
        kDebug() << bracket << c;
        if ( ! brackets.isEmpty() && brackets.top() == c ) {
            brackets.pop();
        }
        else if ( bracket != -1 ) {
            brackets.push(openingBrackets.at(bracket));
        }
        else if ( openingBrackets.contains(c) ) {
            start += 1;
            break;
        }
        
        if ( brackets.isEmpty() && c.isSpace() && ! lastWasSlice ) {
            start += 1;
            break;
        }
        
        if ( sliceChars.contains(c) ) {
            lastWasSlice = true;
        }
        else {
            lastWasSlice = false;
        }
        start--;
    }
    if ( ! ( start < end ) ) {
        return QString();
    }

    QString expression(line.mid(start, end-start));
    expression = expression.trimmed();
    kDebug() << "expression found:" << expression;
    return expression;
}

typedef QPair<Declaration*, int> DeclarationDepthPair;

void VariableController::update()
{
    kDebug() << "update requested";
    DebugSession* d = static_cast<DebugSession*>(parent());
    kDebug() << d->m_commandQueue.length() << "commands in queue";
    DUChainReadLocker lock;
    TopDUContext* topContext = DUChain::self()->chainForDocument(d->currentUrl());
    if ( ! topContext ) {
        kDebug() << "no top context, aborting";
        return;
    }
    CursorInRevision loc = CursorInRevision(d->currentLine(), 0);
    if ( DUContext* currentContext = topContext->findContextAt(loc) ) {
        QList<DeclarationDepthPair> decls = currentContext->allDeclarations(loc, topContext);
        QStringList vars;
        QStringList lateVars;
        foreach ( DeclarationDepthPair dp, decls ) {
            Declaration* d = dp.first;
            if ( ! d ) {
                continue;
            }
            if (  ( d->context() == currentContext || d->context()->type() == DUContext::Function ) 
                 && d->context()->type() != DUContext::Class )
            {
                vars << d->identifier().toString();
            }
        }
        QList<KDevelop::Variable*> variables = KDevelop::ICore::self()->debugController()->variableCollection()
                                     ->locals()->updateLocals(vars);
        foreach ( KDevelop::Variable* v, variables ) {
            v->attachMaybe();
        }
    }
    else {
        kDebug() << "no context found";
    }
}

}


#pragma once

#include "ast.h"

using namespace Python;

QMap<QString, Ast::AstType> astTypes = {
    {QStringLiteral("Expr"), Ast::ExpressionAstType},
    {QStringLiteral("AsyncFunctionDef"), Ast::FunctionDefinitionAstType},
    {QStringLiteral("FunctionDef"), Ast::FunctionDefinitionAstType},
    {QStringLiteral("Assign"), Ast::AssignmentAstType},
    {QStringLiteral("Pass"), Ast::PassAstType},
    {QStringLiteral("Nonlocal"), Ast::NonlocalAstType},
    {QStringLiteral("arguments"), Ast::ArgumentsAstType},
    {QStringLiteral("arg"), Ast::ArgAstType},
    {QStringLiteral("Keyword"), Ast::KeywordAstType},
    {QStringLiteral("ClassDef"), Ast::ClassDefinitionAstType},
    {QStringLiteral("Return"), Ast::ReturnAstType},
    {QStringLiteral("Delete"), Ast::DeleteAstType},
    {QStringLiteral("For"), Ast::ForAstType},
    {QStringLiteral("While"), Ast::WhileAstType},
    {QStringLiteral("If"), Ast::IfAstType},
    {QStringLiteral("With"), Ast::WithAstType},
    {QStringLiteral("WithItem"), Ast::WithItemAstType},
    {QStringLiteral("Raise"), Ast::RaiseAstType},
    {QStringLiteral("Try"), Ast::TryAstType},
    {QStringLiteral("Import"), Ast::ImportAstType},
    {QStringLiteral("ImportFrom"), Ast::ImportFromAstType},
    {QStringLiteral("Global"), Ast::GlobalAstType},
    {QStringLiteral("Break"), Ast::BreakAstType},
    {QStringLiteral("Continue"), Ast::ContinueAstType},
    {QStringLiteral("Assertion"), Ast::AssertionAstType},
    {QStringLiteral("AugmentedAssignment"), Ast::AugmentedAssignmentAstType},
    {QStringLiteral("AnnotationAssignment"), Ast::AnnotationAssignmentAstType},
    {QStringLiteral("Await"), Ast::AwaitAstType},
    {QStringLiteral("Name"), Ast::NameAstType},
    {QStringLiteral("NameConstant"), Ast::NameConstantAstType},
    {QStringLiteral("Constant"), Ast::ConstantAstType},
    {QStringLiteral("Call"), Ast::CallAstType},
    {QStringLiteral("Attribute"), Ast::AttributeAstType},
    {QStringLiteral("DictionaryComprehension"), Ast::DictionaryComprehensionAstType},
    {QStringLiteral("BoolOp"), Ast::BooleanOperationAstType},
    {QStringLiteral("BinOp"), Ast::BinaryOperationAstType},
    {QStringLiteral("UnaryOperation"), Ast::UnaryOperationAstType},
    {QStringLiteral("Lambda"), Ast::LambdaAstType},
    {QStringLiteral("IfExpression"), Ast::IfExpressionAstType},
    {QStringLiteral("Dict"), Ast::DictAstType},
    {QStringLiteral("Set"), Ast::SetAstType},
    {QStringLiteral("ListComprehension"), Ast::ListComprehensionAstType},
    {QStringLiteral("SetComprehension"), Ast::SetComprehensionAstType},
    {QStringLiteral("GeneratorExpression"), Ast::GeneratorExpressionAstType},
    {QStringLiteral("Yield"), Ast::YieldAstType},
    {QStringLiteral("Compare"), Ast::CompareAstType},
    {QStringLiteral("Number"), Ast::NumberAstType},
    {QStringLiteral("String"), Ast::StringAstType},
    {QStringLiteral("JoinedString"), Ast::JoinedStringAstType},
    {QStringLiteral("FormattedValue"), Ast::FormattedValueAstType},
    {QStringLiteral("Bytes"), Ast::BytesAstType},
    {QStringLiteral("Subscript"), Ast::SubscriptAstType},
    {QStringLiteral("Starred"), Ast::StarredAstType},
    {QStringLiteral("List"), Ast::ListAstType},
    {QStringLiteral("Tuple"), Ast::TupleAstType},
    {QStringLiteral("YieldFrom"), Ast::YieldFromAstType},
    {QStringLiteral("Comprehension"), Ast::ComprehensionAstType},
    {QStringLiteral("Slice"), Ast::SliceAstType},
    {QStringLiteral("Ellipsis"), Ast::EllipsisAstType},
    {QStringLiteral("AssignmentExpression"), Ast::AssignmentExpressionAstType},
    {QStringLiteral("Module"), Ast::CodeAstType},
    {QStringLiteral("ExceptionHandler"), Ast::ExceptionHandlerAstType},
    {QStringLiteral("Alias"), Ast::AliasAstType},
};

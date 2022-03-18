#pragma once
#include "fromxml_fwd.h"
#include "nodereader.h"
#include "nodereader_impl.h"

Ast* readTyped(Ast* parent, Python::Ast::AstType astType, Stream& s) {
    switch (astType) {
        case Ast::FunctionDefinitionAstType:
            return NodeReader<FunctionDefinitionAst>(parent).read(s);
        case Ast::AssignmentAstType:
            return NodeReader<AssignmentAst>(parent).read(s);
        case Ast::PassAstType:
            return NodeReader<PassAst>(parent).read(s);
        case Ast::NonlocalAstType:
            return NodeReader<NonlocalAst>(parent).read(s);
        case Ast::ArgumentsAstType:
            return NodeReader<ArgumentsAst>(parent).read(s);
        case Ast::ArgAstType:
            return NodeReader<ArgAst>(parent).read(s);
        case Ast::KeywordAstType:
            return NodeReader<KeywordAst>(parent).read(s);
        case Ast::ClassDefinitionAstType:
            return NodeReader<ClassDefinitionAst>(parent).read(s);
        case Ast::ReturnAstType:
            return NodeReader<ReturnAst>(parent).read(s);
        case Ast::DeleteAstType:
            return NodeReader<DeleteAst>(parent).read(s);
        case Ast::ForAstType:
            return NodeReader<ForAst>(parent).read(s);
        case Ast::WhileAstType:
            return NodeReader<WhileAst>(parent).read(s);
        case Ast::IfAstType:
            return NodeReader<IfAst>(parent).read(s);
        case Ast::WithAstType:
            return NodeReader<WithAst>(parent).read(s);
        case Ast::WithItemAstType:
            return NodeReader<WithItemAst>(parent).read(s);
        case Ast::RaiseAstType:
            return NodeReader<RaiseAst>(parent).read(s);
        case Ast::TryAstType:
            return NodeReader<TryAst>(parent).read(s);
        case Ast::ImportAstType:
            return NodeReader<ImportAst>(parent).read(s);
        case Ast::ImportFromAstType:
            return NodeReader<ImportFromAst>(parent).read(s);
        case Ast::GlobalAstType:
            return NodeReader<GlobalAst>(parent).read(s);
        case Ast::BreakAstType:
            return NodeReader<BreakAst>(parent).read(s);
        case Ast::ContinueAstType:
            return NodeReader<ContinueAst>(parent).read(s);
        case Ast::AssertionAstType:
            return NodeReader<AssertionAst>(parent).read(s);
        case Ast::AugmentedAssignmentAstType:
            return NodeReader<AugmentedAssignmentAst>(parent).read(s);
        case Ast::AnnotationAssignmentAstType:
            return NodeReader<AnnotationAssignmentAst>(parent).read(s);
        case Ast::AwaitAstType:
            return NodeReader<AwaitAst>(parent).read(s);
        case Ast::NameAstType:
            return NodeReader<NameAst>(parent).read(s);
        case Ast::NameConstantAstType:
            return NodeReader<NameConstantAst>(parent).read(s);
        case Ast::ConstantAstType:
            return NodeReader<ConstantAst>(parent).read(s);
        case Ast::CallAstType:
            return NodeReader<CallAst>(parent).read(s);
        case Ast::AttributeAstType:
            return NodeReader<AttributeAst>(parent).read(s);
        case Ast::DictionaryComprehensionAstType:
            return NodeReader<DictionaryComprehensionAst>(parent).read(s);
        case Ast::BooleanOperationAstType:
            return NodeReader<BooleanOperationAst>(parent).read(s);
        case Ast::BinaryOperationAstType:
            return NodeReader<BinaryOperationAst>(parent).read(s);
        case Ast::UnaryOperationAstType:
            return NodeReader<UnaryOperationAst>(parent).read(s);
        case Ast::LambdaAstType:
            return NodeReader<LambdaAst>(parent).read(s);
        case Ast::IfExpressionAstType:
            return NodeReader<IfExpressionAst>(parent).read(s);
        case Ast::DictAstType:
            return NodeReader<DictAst>(parent).read(s);
        case Ast::SetAstType:
            return NodeReader<SetAst>(parent).read(s);
        case Ast::ListComprehensionAstType:
            return NodeReader<ListComprehensionAst>(parent).read(s);
        case Ast::SetComprehensionAstType:
            return NodeReader<SetComprehensionAst>(parent).read(s);
        case Ast::GeneratorExpressionAstType:
            return NodeReader<GeneratorExpressionAst>(parent).read(s);
        case Ast::YieldAstType:
            return NodeReader<YieldAst>(parent).read(s);
        case Ast::CompareAstType:
            return NodeReader<CompareAst>(parent).read(s);
        case Ast::NumberAstType:
            return NodeReader<NumberAst>(parent).read(s);
        case Ast::StringAstType:
            return NodeReader<StringAst>(parent).read(s);
        case Ast::JoinedStringAstType:
            return NodeReader<JoinedStringAst>(parent).read(s);
        case Ast::FormattedValueAstType:
            return NodeReader<FormattedValueAst>(parent).read(s);
        case Ast::BytesAstType:
            return NodeReader<BytesAst>(parent).read(s);
        case Ast::SubscriptAstType:
            return NodeReader<SubscriptAst>(parent).read(s);
        case Ast::StarredAstType:
            return NodeReader<StarredAst>(parent).read(s);
        case Ast::ListAstType:
            return NodeReader<ListAst>(parent).read(s);
        case Ast::TupleAstType:
            return NodeReader<TupleAst>(parent).read(s);
        case Ast::YieldFromAstType:
            return NodeReader<YieldFromAst>(parent).read(s);
        case Ast::ComprehensionAstType:
            return NodeReader<ComprehensionAst>(parent).read(s);
        case Ast::SliceAstType:
            return NodeReader<SliceAst>(parent).read(s);
        case Ast::EllipsisAstType:
            return NodeReader<EllipsisAst>(parent).read(s);
        case Ast::AssignmentExpressionAstType:
            return NodeReader<AssignmentExpressionAst>(parent).read(s);
        case Ast::CodeAstType:
            return NodeReader<CodeAst>(parent).read(s);
        case Ast::ExceptionHandlerAstType:
            return NodeReader<ExceptionHandlerAst>(parent).read(s);
        case Ast::AliasAstType:
            return NodeReader<AliasAst>(parent).read(s);
        case Ast::ExpressionAstType:
            return NodeReader<ExpressionAst>(parent).read(s);
        case Ast::LastStatementType:
        case Ast::StatementAstType:
        case Ast::LastExpressionType:
        case Ast::IdentifierAstType:
        case Ast::LastAstType:
            break;
    };
    return nullptr;
}

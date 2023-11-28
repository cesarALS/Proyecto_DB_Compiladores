// Generated from C:/aCompiladores/Tareas/Proyecto final/db_api_project/Query.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link QueryParser}.
 */
public interface QueryListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code compareExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void enterCompareExp(QueryParser.CompareExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code compareExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void exitCompareExp(QueryParser.CompareExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void enterParenExp(QueryParser.ParenExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void exitParenExp(QueryParser.ParenExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void enterLogicalExp(QueryParser.LogicalExpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalExp}
	 * labeled alternative in {@link QueryParser#query}.
	 * @param ctx the parse tree
	 */
	void exitLogicalExp(QueryParser.LogicalExpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code boolean}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void enterBoolean(QueryParser.BooleanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code boolean}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void exitBoolean(QueryParser.BooleanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code null}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void enterNull(QueryParser.NullContext ctx);
	/**
	 * Exit a parse tree produced by the {@code null}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void exitNull(QueryParser.NullContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void enterString(QueryParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void exitString(QueryParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code double}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void enterDouble(QueryParser.DoubleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code double}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void exitDouble(QueryParser.DoubleContext ctx);
	/**
	 * Enter a parse tree produced by the {@code long}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void enterLong(QueryParser.LongContext ctx);
	/**
	 * Exit a parse tree produced by the {@code long}
	 * labeled alternative in {@link QueryParser#value}.
	 * @param ctx the parse tree
	 */
	void exitLong(QueryParser.LongContext ctx);
}
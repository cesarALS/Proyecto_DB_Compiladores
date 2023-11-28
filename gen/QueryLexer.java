// Generated from C:/aCompiladores/Tareas/Proyecto final/db_api_project/Query.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class QueryLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, LOGICAL_OPERATOR=4, BOOLEAN=5, EQ=6, NE=7, ATTRNAME=8, 
		STRING=9, DOUBLE=10, INT=11, EXP=12, WS=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "LOGICAL_OPERATOR", "BOOLEAN", "EQ", "NE", "ATTRNAME", 
			"ATTR_NAME_CHAR", "DIGIT", "ALPHA", "STRING", "ESC", "UNICODE", "HEX", 
			"DOUBLE", "INT", "EXP", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'-'", null, null, "'eq'", "'ne'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "LOGICAL_OPERATOR", "BOOLEAN", "EQ", "NE", "ATTRNAME", 
			"STRING", "DOUBLE", "INT", "EXP", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public QueryLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Query.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\r\u0090\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u00033\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004>\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0005\u0007H\b\u0007\n\u0007"+
		"\f\u0007K\t\u0007\u0001\b\u0001\b\u0001\b\u0003\bP\b\b\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000bY\b\u000b"+
		"\n\u000b\f\u000b\\\t\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0003\fc\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0003\u000fn\b\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0004\u000fs\b\u000f\u000b\u000f\f\u000ft\u0001\u000f"+
		"\u0003\u000fx\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010"+
		"}\b\u0010\n\u0010\f\u0010\u0080\t\u0010\u0003\u0010\u0082\b\u0010\u0001"+
		"\u0011\u0001\u0011\u0003\u0011\u0086\b\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0004\u0012\u008b\b\u0012\u000b\u0012\f\u0012\u008c\u0001\u0012"+
		"\u0001\u0012\u0000\u0000\u0013\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\u0000\u0013\u0000\u0015"+
		"\u0000\u0017\t\u0019\u0000\u001b\u0000\u001d\u0000\u001f\n!\u000b#\f%"+
		"\r\u0001\u0000\n\u0003\u0000--::__\u0002\u0000AZaz\u0002\u0000\"\"\\\\"+
		"\b\u0000\"\"//\\\\bbffnnrrtt\u0003\u000009AFaf\u0001\u000009\u0001\u0000"+
		"19\u0002\u0000EEee\u0002\u0000++--\u0002\u0000\t\t  \u0098\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0001"+
		"\'\u0001\u0000\u0000\u0000\u0003)\u0001\u0000\u0000\u0000\u0005+\u0001"+
		"\u0000\u0000\u0000\u00072\u0001\u0000\u0000\u0000\t=\u0001\u0000\u0000"+
		"\u0000\u000b?\u0001\u0000\u0000\u0000\rB\u0001\u0000\u0000\u0000\u000f"+
		"E\u0001\u0000\u0000\u0000\u0011O\u0001\u0000\u0000\u0000\u0013Q\u0001"+
		"\u0000\u0000\u0000\u0015S\u0001\u0000\u0000\u0000\u0017U\u0001\u0000\u0000"+
		"\u0000\u0019_\u0001\u0000\u0000\u0000\u001bd\u0001\u0000\u0000\u0000\u001d"+
		"j\u0001\u0000\u0000\u0000\u001fm\u0001\u0000\u0000\u0000!\u0081\u0001"+
		"\u0000\u0000\u0000#\u0083\u0001\u0000\u0000\u0000%\u008a\u0001\u0000\u0000"+
		"\u0000\'(\u0005(\u0000\u0000(\u0002\u0001\u0000\u0000\u0000)*\u0005)\u0000"+
		"\u0000*\u0004\u0001\u0000\u0000\u0000+,\u0005-\u0000\u0000,\u0006\u0001"+
		"\u0000\u0000\u0000-.\u0005a\u0000\u0000./\u0005n\u0000\u0000/3\u0005d"+
		"\u0000\u000001\u0005o\u0000\u000013\u0005r\u0000\u00002-\u0001\u0000\u0000"+
		"\u000020\u0001\u0000\u0000\u00003\b\u0001\u0000\u0000\u000045\u0005t\u0000"+
		"\u000056\u0005r\u0000\u000067\u0005u\u0000\u00007>\u0005e\u0000\u0000"+
		"89\u0005f\u0000\u00009:\u0005a\u0000\u0000:;\u0005l\u0000\u0000;<\u0005"+
		"s\u0000\u0000<>\u0005e\u0000\u0000=4\u0001\u0000\u0000\u0000=8\u0001\u0000"+
		"\u0000\u0000>\n\u0001\u0000\u0000\u0000?@\u0005e\u0000\u0000@A\u0005q"+
		"\u0000\u0000A\f\u0001\u0000\u0000\u0000BC\u0005n\u0000\u0000CD\u0005e"+
		"\u0000\u0000D\u000e\u0001\u0000\u0000\u0000EI\u0003\u0015\n\u0000FH\u0003"+
		"\u0011\b\u0000GF\u0001\u0000\u0000\u0000HK\u0001\u0000\u0000\u0000IG\u0001"+
		"\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\u0010\u0001\u0000\u0000"+
		"\u0000KI\u0001\u0000\u0000\u0000LP\u0007\u0000\u0000\u0000MP\u0003\u0013"+
		"\t\u0000NP\u0003\u0015\n\u0000OL\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000ON\u0001\u0000\u0000\u0000P\u0012\u0001\u0000\u0000\u0000"+
		"QR\u000209\u0000R\u0014\u0001\u0000\u0000\u0000ST\u0007\u0001\u0000\u0000"+
		"T\u0016\u0001\u0000\u0000\u0000UZ\u0005\"\u0000\u0000VY\u0003\u0019\f"+
		"\u0000WY\b\u0002\u0000\u0000XV\u0001\u0000\u0000\u0000XW\u0001\u0000\u0000"+
		"\u0000Y\\\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000Z[\u0001\u0000"+
		"\u0000\u0000[]\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000]^\u0005"+
		"\"\u0000\u0000^\u0018\u0001\u0000\u0000\u0000_b\u0005\\\u0000\u0000`c"+
		"\u0007\u0003\u0000\u0000ac\u0003\u001b\r\u0000b`\u0001\u0000\u0000\u0000"+
		"ba\u0001\u0000\u0000\u0000c\u001a\u0001\u0000\u0000\u0000de\u0005u\u0000"+
		"\u0000ef\u0003\u001d\u000e\u0000fg\u0003\u001d\u000e\u0000gh\u0003\u001d"+
		"\u000e\u0000hi\u0003\u001d\u000e\u0000i\u001c\u0001\u0000\u0000\u0000"+
		"jk\u0007\u0004\u0000\u0000k\u001e\u0001\u0000\u0000\u0000ln\u0005-\u0000"+
		"\u0000ml\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0001\u0000"+
		"\u0000\u0000op\u0003!\u0010\u0000pr\u0005.\u0000\u0000qs\u0007\u0005\u0000"+
		"\u0000rq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000tr\u0001\u0000"+
		"\u0000\u0000tu\u0001\u0000\u0000\u0000uw\u0001\u0000\u0000\u0000vx\u0003"+
		"#\u0011\u0000wv\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000x \u0001"+
		"\u0000\u0000\u0000y\u0082\u00050\u0000\u0000z~\u0007\u0006\u0000\u0000"+
		"{}\u0007\u0005\u0000\u0000|{\u0001\u0000\u0000\u0000}\u0080\u0001\u0000"+
		"\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000"+
		"\u007f\u0082\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0081"+
		"y\u0001\u0000\u0000\u0000\u0081z\u0001\u0000\u0000\u0000\u0082\"\u0001"+
		"\u0000\u0000\u0000\u0083\u0085\u0007\u0007\u0000\u0000\u0084\u0086\u0007"+
		"\b\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000"+
		"\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u0088\u0003!\u0010"+
		"\u0000\u0088$\u0001\u0000\u0000\u0000\u0089\u008b\u0007\t\u0000\u0000"+
		"\u008a\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000"+
		"\u008c\u008a\u0001\u0000\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000"+
		"\u008d\u008e\u0001\u0000\u0000\u0000\u008e\u008f\u0006\u0012\u0000\u0000"+
		"\u008f&\u0001\u0000\u0000\u0000\u000f\u00002=IOXZbmtw~\u0081\u0085\u008c"+
		"\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
"""
    pygments.lexers._postgres_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Self-updating data files for PostgreSQL lexer.

    Run with `python -I` to update itself.

    :copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Autogenerated: please edit them if you like wasting your time.

KEYWORDS = (
    'ABORT',
    'ABSOLUTE',
    'ACCESS',
    'ACTION',
    'ADD',
    'ADMIN',
    'AFTER',
    'AGGREGATE',
    'ALL',
    'ALSO',
    'ALTER',
    'ALWAYS',
    'ANALYSE',
    'ANALYZE',
    'AND',
    'ANY',
    'ARRAY',
    'AS',
    'ASC',
    'ASENSITIVE',
    'ASSERTION',
    'ASSIGNMENT',
    'ASYMMETRIC',
    'AT',
    'ATOMIC',
    'ATTACH',
    'ATTRIBUTE',
    'AUTHORIZATION',
    'BACKWARD',
    'BEFORE',
    'BEGIN',
    'BETWEEN',
    'BIGINT',
    'BINARY',
    'BIT',
    'BOOLEAN',
    'BOTH',
    'BREADTH',
    'BY',
    'CACHE',
    'CALL',
    'CALLED',
    'CASCADE',
    'CASCADED',
    'CASE',
    'CAST',
    'CATALOG',
    'CHAIN',
    'CHAR',
    'CHARACTER',
    'CHARACTERISTICS',
    'CHECK',
    'CHECKPOINT',
    'CLASS',
    'CLOSE',
    'CLUSTER',
    'COALESCE',
    'COLLATE',
    'COLLATION',
    'COLUMN',
    'COLUMNS',
    'COMMENT',
    'COMMENTS',
    'COMMIT',
    'COMMITTED',
    'COMPRESSION',
    'CONCURRENTLY',
    'CONFIGURATION',
    'CONFLICT',
    'CONNECTION',
    'CONSTRAINT',
    'CONSTRAINTS',
    'CONTENT',
    'CONTINUE',
    'CONVERSION',
    'COPY',
    'COST',
    'CREATE',
    'CROSS',
    'CSV',
    'CUBE',
    'CURRENT',
    'CURRENT_CATALOG',
    'CURRENT_DATE',
    'CURRENT_ROLE',
    'CURRENT_SCHEMA',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'CURRENT_USER',
    'CURSOR',
    'CYCLE',
    'DATA',
    'DATABASE',
    'DAY',
    'DEALLOCATE',
    'DEC',
    'DECIMAL',
    'DECLARE',
    'DEFAULT',
    'DEFAULTS',
    'DEFERRABLE',
    'DEFERRED',
    'DEFINER',
    'DELETE',
    'DELIMITER',
    'DELIMITERS',
    'DEPENDS',
    'DEPTH',
    'DESC',
    'DETACH',
    'DICTIONARY',
    'DISABLE',
    'DISCARD',
    'DISTINCT',
    'DO',
    'DOCUMENT',
    'DOMAIN',
    'DOUBLE',
    'DROP',
    'EACH',
    'ELSE',
    'ENABLE',
    'ENCODING',
    'ENCRYPTED',
    'END',
    'ENUM',
    'ESCAPE',
    'EVENT',
    'EXCEPT',
    'EXCLUDE',
    'EXCLUDING',
    'EXCLUSIVE',
    'EXECUTE',
    'EXISTS',
    'EXPLAIN',
    'EXPRESSION',
    'EXTENSION',
    'EXTERNAL',
    'EXTRACT',
    'FALSE',
    'FAMILY',
    'FETCH',
    'FILTER',
    'FINALIZE',
    'FIRST',
    'FLOAT',
    'FOLLOWING',
    'FOR',
    'FORCE',
    'FOREIGN',
    'FORWARD',
    'FREEZE',
    'FROM',
    'FULL',
    'FUNCTION',
    'FUNCTIONS',
    'GENERATED',
    'GLOBAL',
    'GRANT',
    'GRANTED',
    'GREATEST',
    'GROUP',
    'GROUPING',
    'GROUPS',
    'HANDLER',
    'HAVING',
    'HEADER',
    'HOLD',
    'HOUR',
    'IDENTITY',
    'IF',
    'ILIKE',
    'IMMEDIATE',
    'IMMUTABLE',
    'IMPLICIT',
    'IMPORT',
    'IN',
    'INCLUDE',
    'INCLUDING',
    'INCREMENT',
    'INDEX',
    'INDEXES',
    'INHERIT',
    'INHERITS',
    'INITIALLY',
    'INLINE',
    'INNER',
    'INOUT',
    'INPUT',
    'INSENSITIVE',
    'INSERT',
    'INSTEAD',
    'INT',
    'INTEGER',
    'INTERSECT',
    'INTERVAL',
    'INTO',
    'INVOKER',
    'IS',
    'ISNULL',
    'ISOLATION',
    'JOIN',
    'KEY',
    'LABEL',
    'LANGUAGE',
    'LARGE',
    'LAST',
    'LATERAL',
    'LEADING',
    'LEAKPROOF',
    'LEAST',
    'LEFT',
    'LEVEL',
    'LIKE',
    'LIMIT',
    'LISTEN',
    'LOAD',
    'LOCAL',
    'LOCALTIME',
    'LOCALTIMESTAMP',
    'LOCATION',
    'LOCK',
    'LOCKED',
    'LOGGED',
    'MAPPING',
    'MATCH',
    'MATERIALIZED',
    'MAXVALUE',
    'METHOD',
    'MINUTE',
    'MINVALUE',
    'MODE',
    'MONTH',
    'MOVE',
    'NAME',
    'NAMES',
    'NATIONAL',
    'NATURAL',
    'NCHAR',
    'NEW',
    'NEXT',
    'NFC',
    'NFD',
    'NFKC',
    'NFKD',
    'NO',
    'NONE',
    'NORMALIZE',
    'NORMALIZED',
    'NOT',
    'NOTHING',
    'NOTIFY',
    'NOTNULL',
    'NOWAIT',
    'NULL',
    'NULLIF',
    'NULLS',
    'NUMERIC',
    'OBJECT',
    'OF',
    'OFF',
    'OFFSET',
    'OIDS',
    'OLD',
    'ON',
    'ONLY',
    'OPERATOR',
    'OPTION',
    'OPTIONS',
    'OR',
    'ORDER',
    'ORDINALITY',
    'OTHERS',
    'OUT',
    'OUTER',
    'OVER',
    'OVERLAPS',
    'OVERLAY',
    'OVERRIDING',
    'OWNED',
    'OWNER',
    'PARALLEL',
    'PARSER',
    'PARTIAL',
    'PARTITION',
    'PASSING',
    'PASSWORD',
    'PLACING',
    'PLANS',
    'POLICY',
    'POSITION',
    'PRECEDING',
    'PRECISION',
    'PREPARE',
    'PREPARED',
    'PRESERVE',
    'PRIMARY',
    'PRIOR',
    'PRIVILEGES',
    'PROCEDURAL',
    'PROCEDURE',
    'PROCEDURES',
    'PROGRAM',
    'PUBLICATION',
    'QUOTE',
    'RANGE',
    'READ',
    'REAL',
    'REASSIGN',
    'RECHECK',
    'RECURSIVE',
    'REF',
    'REFERENCES',
    'REFERENCING',
    'REFRESH',
    'REINDEX',
    'RELATIVE',
    'RELEASE',
    'RENAME',
    'REPEATABLE',
    'REPLACE',
    'REPLICA',
    'RESET',
    'RESTART',
    'RESTRICT',
    'RETURN',
    'RETURNING',
    'RETURNS',
    'REVOKE',
    'RIGHT',
    'ROLE',
    'ROLLBACK',
    'ROLLUP',
    'ROUTINE',
    'ROUTINES',
    'ROW',
    'ROWS',
    'RULE',
    'SAVEPOINT',
    'SCHEMA',
    'SCHEMAS',
    'SCROLL',
    'SEARCH',
    'SECOND',
    'SECURITY',
    'SELECT',
    'SEQUENCE',
    'SEQUENCES',
    'SERIALIZABLE',
    'SERVER',
    'SESSION',
    'SESSION_USER',
    'SET',
    'SETOF',
    'SETS',
    'SHARE',
    'SHOW',
    'SIMILAR',
    'SIMPLE',
    'SKIP',
    'SMALLINT',
    'SNAPSHOT',
    'SOME',
    'SQL',
    'STABLE',
    'STANDALONE',
    'START',
    'STATEMENT',
    'STATISTICS',
    'STDIN',
    'STDOUT',
    'STORAGE',
    'STORED',
    'STRICT',
    'STRIP',
    'SUBSCRIPTION',
    'SUBSTRING',
    'SUPPORT',
    'SYMMETRIC',
    'SYSID',
    'SYSTEM',
    'TABLE',
    'TABLES',
    'TABLESAMPLE',
    'TABLESPACE',
    'TEMP',
    'TEMPLATE',
    'TEMPORARY',
    'TEXT',
    'THEN',
    'TIES',
    'TIME',
    'TIMESTAMP',
    'TO',
    'TRAILING',
    'TRANSACTION',
    'TRANSFORM',
    'TREAT',
    'TRIGGER',
    'TRIM',
    'TRUE',
    'TRUNCATE',
    'TRUSTED',
    'TYPE',
    'TYPES',
    'UESCAPE',
    'UNBOUNDED',
    'UNCOMMITTED',
    'UNENCRYPTED',
    'UNION',
    'UNIQUE',
    'UNKNOWN',
    'UNLISTEN',
    'UNLOGGED',
    'UNTIL',
    'UPDATE',
    'USER',
    'USING',
    'VACUUM',
    'VALID',
    'VALIDATE',
    'VALIDATOR',
    'VALUE',
    'VALUES',
    'VARCHAR',
    'VARIADIC',
    'VARYING',
    'VERBOSE',
    'VERSION',
    'VIEW',
    'VIEWS',
    'VOLATILE',
    'WHEN',
    'WHERE',
    'WHITESPACE',
    'WINDOW',
    'WITH',
    'WITHIN',
    'WITHOUT',
    'WORK',
    'WRAPPER',
    'WRITE',
    'XML',
    'XMLATTRIBUTES',
    'XMLCONCAT',
    'XMLELEMENT',
    'XMLEXISTS',
    'XMLFOREST',
    'XMLNAMESPACES',
    'XMLPARSE',
    'XMLPI',
    'XMLROOT',
    'XMLSERIALIZE',
    'XMLTABLE',
    'YEAR',
    'YES',
    'ZONE',
)

DATATYPES = (
    'bigint',
    'bigserial',
    'bit',
    'bit varying',
    'bool',
    'boolean',
    'box',
    'bytea',
    'char',
    'character',
    'character varying',
    'cidr',
    'circle',
    'date',
    'decimal',
    'double precision',
    'float4',
    'float8',
    'inet',
    'int',
    'int2',
    'int4',
    'int8',
    'integer',
    'interval',
    'json',
    'jsonb',
    'line',
    'lseg',
    'macaddr',
    'macaddr8',
    'money',
    'numeric',
    'path',
    'pg_lsn',
    'pg_snapshot',
    'point',
    'polygon',
    'real',
    'serial',
    'serial2',
    'serial4',
    'serial8',
    'smallint',
    'smallserial',
    'text',
    'time',
    'timestamp',
    'timestamptz',
    'timetz',
    'tsquery',
    'tsvector',
    'txid_snapshot',
    'uuid',
    'varbit',
    'varchar',
    'with time zone',
    'without time zone',
    'xml',
)

PSEUDO_TYPES = (
    'any',
    'anyarray',
    'anycompatible',
    'anycompatiblearray',
    'anycompatiblemultirange',
    'anycompatiblenonarray',
    'anycompatiblerange',
    'anyelement',
    'anyenum',
    'anymultirange',
    'anynonarray',
    'anyrange',
    'cstring',
    'event_trigger',
    'fdw_handler',
    'index_am_handler',
    'internal',
    'language_handler',
    'pg_ddl_command',
    'record',
    'table_am_handler',
    'trigger',
    'tsm_handler',
    'unknown',
    'void',
)

# Remove 'trigger' from types
PSEUDO_TYPES = tuple(sorted(set(PSEUDO_TYPES) - set(map(str.lower, KEYWORDS))))

PLPGSQL_KEYWORDS = (
    'ALIAS', 'CONSTANT', 'DIAGNOSTICS', 'ELSIF', 'EXCEPTION', 'EXIT',
    'FOREACH', 'GET', 'LOOP', 'NOTICE', 'OPEN', 'PERFORM', 'QUERY', 'RAISE',
    'RETURN', 'REVERSE', 'SQLSTATE', 'WHILE',
)

# Most of these keywords are from ExplainNode function
# in src/backend/commands/explain.c

EXPLAIN_KEYWORDS = (
    'Aggregate',
    'Append',
    'Bitmap Heap Scan',
    'Bitmap Index Scan',
    'BitmapAnd',
    'BitmapOr',
    'CTE Scan',
    'Custom Scan',
    'Delete',
    'Foreign Scan',
    'Function Scan',
    'Gather Merge',
    'Gather',
    'Group',
    'GroupAggregate',
    'Hash Join',
    'Hash',
    'HashAggregate',
    'Incremental Sort',
    'Index Only Scan',
    'Index Scan',
    'Insert',
    'Limit',
    'LockRows',
    'Materialize',
    'Memoize',
    'Merge Append',
    'Merge Join',
    'Merge',
    'MixedAggregate',
    'Named Tuplestore Scan',
    'Nested Loop',
    'ProjectSet',
    'Recursive Union',
    'Result',
    'Sample Scan',
    'Seq Scan',
    'SetOp',
    'Sort',
    'SubPlan',
    'Subquery Scan',
    'Table Function Scan',
    'Tid Range Scan',
    'Tid Scan',
    'Unique',
    'Update',
    'Values Scan',
    'WindowAgg',
    'WorkTable Scan',
)


if __name__ == '__main__':  # pragma: no cover
    import re
    from urllib.request import urlopen

    from pygments.util import format_lines

    # One man's constant is another man's variable.
    SOURCE_URL = 'https://github.com/postgres/postgres/raw/master'
    KEYWORDS_URL = SOURCE_URL + '/src/include/parser/kwlist.h'
    DATATYPES_URL = SOURCE_URL + '/doc/src/sgml/datatype.sgml'

    def update_myself():
        content = urlopen(DATATYPES_URL).read().decode('utf-8', errors='ignore')
        data_file = list(content.splitlines())
        datatypes = parse_datatypes(data_file)
        pseudos = parse_pseudos(data_file)

        content = urlopen(KEYWORDS_URL).read().decode('utf-8', errors='ignore')
        keywords = parse_keywords(content)

        update_consts(__file__, 'DATATYPES', datatypes)
        update_consts(__file__, 'PSEUDO_TYPES', pseudos)
        update_consts(__file__, 'KEYWORDS', keywords)

    def parse_keywords(f):
        kw = []
        for m in re.finditer(r'PG_KEYWORD\("(.+?)"', f):
            kw.append(m.group(1).upper())

        if not kw:
            raise ValueError('no keyword found')

        kw.sort()
        return kw

    def parse_datatypes(f):
        dt = set()
        for line in f:
            if '<sect1' in line:
                break
            if '<entry><type>' not in line:
                continue

            # Parse a string such as
            # time [ (<replaceable>p</replaceable>) ] [ without time zone ]
            # into types "time" and "without time zone"

            # remove all the tags
            line = re.sub("<replaceable>[^<]+</replaceable>", "", line)
            line = re.sub("<[^>]+>", "", line)

            # Drop the parts containing braces
            for tmp in [t for tmp in line.split('[')
                        for t in tmp.split(']') if "(" not in t]:
                for t in tmp.split(','):
                    t = t.strip()
                    if not t: continue
                    dt.add(" ".join(t.split()))

        dt = list(dt)
        dt.sort()
        return dt

    def parse_pseudos(f):
        dt = []
        re_start = re.compile(r'\s*<table id="datatype-pseudotypes-table">')
        re_entry = re.compile(r'\s*<entry><type>(.+?)</type></entry>')
        re_end = re.compile(r'\s*</table>')

        f = iter(f)
        for line in f:
            if re_start.match(line) is not None:
                break
        else:
            raise ValueError('pseudo datatypes table not found')

        for line in f:
            m = re_entry.match(line)
            if m is not None:
                dt.append(m.group(1))

            if re_end.match(line) is not None:
                break
        else:
            raise ValueError('end of pseudo datatypes table not found')

        if not dt:
            raise ValueError('pseudo datatypes not found')

        dt.sort()
        return dt

    def update_consts(filename, constname, content):
        with open(filename, encoding='utf-8') as f:
            data = f.read()

        # Line to start/end inserting
        re_match = re.compile(r'^%s\s*=\s*\($.*?^\s*\)$' % constname, re.M | re.S)
        m = re_match.search(data)
        if not m:
            raise ValueError('Could not find existing definition for %s' %
                             (constname,))

        new_block = format_lines(constname, content)
        data = data[:m.start()] + new_block + data[m.end():]

        with open(filename, 'w', encoding='utf-8', newline='\n') as f:
            f.write(data)

    update_myself()

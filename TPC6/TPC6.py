import ply.lex as lex

tokens = (
    'INT',
    'VAR',
    'PONTOEVIRGULA',
    'FUNCAO',
    'NOMEFUNCAO',
    'ABRIRPARENTISES',
    'FECHARPARENTISES',
    'ARGUMENTO',
    'VIRGULA',
    'ABRIRCHAVETA',
    'FECHARCHAVETA',
    'IGUAL',
    'NUMERO',
    'WHILE',
    'COMPARADORES',
    'OPERADORES',
    'PROGRAMA',
    'FOR',
    'IN',
    'RANGE',
    'IF',
    'ABRIRPARENTISESRETO',
    'FECHARPARENTISESRETO'
)

# Regular expressions
t_ignore_COMENTARIODEUMALINHA = r'\/\/.*?\n'
t_ignore_COMENTARIOVARIASLINHAS = r'\/\*(.|\n)*?\*\/'
t_ignore = ' \t\n'

t_INT = r'int'
t_PROGRAMA = r'program\s\w+'
t_PONTOEVIRGULA = r'\;'
t_FUNCAO = r'function '
t_NOMEFUNCAO = r'\w+(?=\()'
t_ABRIRPARENTISES = r'\('
t_FECHARPARENTISES = r'\)'
t_ARGUMENTO = r'[A-Za-z]+\w*(?=\)|\,)'
t_VIRGULA = r'\,'
t_RANGE = r'\[\d+\.\.\d+\]'
t_ABRIRCHAVETA = r'\{'
t_FECHARCHAVETA = r'\}'
t_IGUAL = r'\='
t_NUMERO = r'[+-]?\d+'
t_WHILE = r'while'
t_COMPARADORES = r'(<|>|==|>=|<=)'
t_OPERADORES = r'(\+|\-|\*|\/)'
t_FOR = r'for'
t_IN = r'in'
t_IF = r'if'
t_ABRIRPARENTISESRETO = r'\['
t_FECHARPARENTISESRETO = r'\]'
t_VAR = r'\w+'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test data
data1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

data2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''


lexer.input(data1)

while tok := lexer.token():
    print(tok)

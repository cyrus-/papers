def process(filename):
  with open(filename) as f:
    grammar_spec_lines = f.readlines()

  syntax = []
  macros = []
  n_cols = None
  n_read = 0
  read = []
  for line in grammar_spec_lines:
    if n_cols is None:
      n_cols = int(line)
      continue
    if line[0:2] == "  ":
      macros.append(line[2:-1])
      continue
    if line == "\n" or line[0] == "%":
      continue
    read.append(line[:-1])
    n_read += 1
    if n_read == n_cols:
      syntax.append(read)
      n_read = 0
      read = []

  return syntax, macros

ossyntax, osmacros = process("grammar-spec.tex")
ssyntax, smacros = process("syntax-spec-s.tex")
qsyntax, qmacros = process("syntax-spec-q.tex")
esyntax, emacros = process("syntax-spec-e.tex")
auxsyntax, auxmacros = process("syntax-spec-aux.tex")
isyntax, imacros = process("syntax-spec-i.tex")

excsyntax, excmacros = process("example-conc.tex")
exasyntax, examacros = process("example-abs.tex")

def pad_to_same_length(a, b, p):
  len_difference = len(b) - len(a)
  if len_difference > 0: # b bigger
    a.extend([p]*len_difference)
  elif len_difference < 0: # a bigger
    b.extend([p]*abs(len_difference))

def combine(left, right):
  pad_to_same_length(left, right, None)
  left_n_cols = len(left[0])
  right_n_cols = len(right[0])
  combined = [ ]
  for l, r in zip(left, right):
    if l is None:
      l = ["~"]*left_n_cols
    if r is None:
      r = ["~"]*right_n_cols
    c = list(l)
    c.extend(r)
    combined.append(c)
  return combined

syntax_SL = ssyntax
syntax_OSL = combine(ossyntax, qsyntax)
syntax_EL = esyntax#combine(esyntax, auxsyntax)
syntax_IL = isyntax
example = combine(excsyntax, exasyntax)
smacros.extend(qmacros)
smacros.extend(emacros)
smacros.extend(auxmacros)
smacros.extend(imacros)
smacros.extend(osmacros)
smacros.extend(excmacros)
smacros.extend(examacros)
macros = smacros

def generate_table(syntax):
  n_cols = len(syntax[0])
  if n_cols == 1:
    table_code = r"$"
  else:
    table_code = r"\begin{tabular}{" + r">{$}l<{$}" * len(syntax[0]) + "}\n"
  for row in syntax:
    print "ROW", row
    table_code += "&\n".join(row)
    table_code += "\\\\\n"
  if n_cols == 1:
    table_code += r"$"
  else:
    table_code += r"\end{tabular}"
  return table_code

table_SL = generate_table(syntax_SL)
table_OSL = generate_table(syntax_OSL)
table_EL = generate_table(syntax_EL)
table_IL = generate_table(syntax_IL)
table_ex = generate_table(example)

macro_code = "\n".join(macros)

def write(str, filename):
  with open(filename, 'w') as f:
    f.write(str)

write(macro_code, "macros-catlam.tex")
write(table_SL, "syntax-table-SL.tex")
write(table_EL, "syntax-table-EL.tex")
write(table_IL, "syntax-table-IL.tex")
write(table_ex, "example-table.tex")

print macro_code
#print table_code
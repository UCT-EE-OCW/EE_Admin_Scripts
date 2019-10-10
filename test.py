from fdfgen import forge_fdf
from subprocess import Popen, PIPE

fields = [("namea", "foo"),
          ("Pet", "bar")]
fdf = forge_fdf("", fields, [], [], [])
pdftk = ["pdftk", "FormsTest.pdf", "fill_form", "-",
          "output", "out.pdf", "flatten"]
proc = Popen(pdftk, stdin=PIPE)
output = proc.communicate(input=fdf)
if output[1]:
    raise IOError(output[1])
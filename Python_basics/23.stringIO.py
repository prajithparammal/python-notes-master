import StringIO
message = 'This is just a normal string'
f = StringIO.StringIO(message)
f.read()
f.write('Second line written to the file like object')
f.seek(0)
f.read()

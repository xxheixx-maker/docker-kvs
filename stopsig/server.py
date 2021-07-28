import os, flask, signal, sys
PORT = int(os.environ['PORT'])

a = 123
b = 'abc'
f = 1.2345

def handle_signal(signal_number, stack_frame):
  # formatを使った書き方
  print('{} and {}'.format(a,b))
  # f文字列を使った書き方
  print(f'graceful shutdowm. sig number:{signal_number}')
  # 中央寄せ
  print(f'graceful shutdowm. sig number:{signal_number:_^8}')
  # 置換フィールドのネスト（forとの組み合わせ）
  for i in range(5):
    print(f'res:{f:.{i}f}')
  sys.exit(0)
signal.signal(signal.SIGINT, handle_signal)

app = flask.Flask('app server')
@app.route('/api/v1/hello')
def index1():
  return 'hello api Dockerfile'
@app.route('/')
def index2():
  return 'hello root Dockerfile'
app.run(debug=True, host='0.0.0.0', port=PORT)

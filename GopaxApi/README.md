# GopaxApi

GopaxApi Link

+ [GopaxApi REST API Documentation](https://gopax.github.io/API/index.html)
+ [GopaxApi WebSocket Documentation](https://gopax.github.io/wsapi/index.html)

<br>

+ #### Sample Python Source code

<details>
<summary>JavaScript</summary>
<div markdown="1">

```py
import base64, hashlib, hmac, json, requests, time

API_KEY = '<입력하세요>'
SECRET = '<입력하세요>'


def call(need_auth, method, path, body_json=None, recv_window=None):
  method = method.upper()
  if need_auth:
    timestamp = str(int(time.time() * 1000))
    include_querystring = method == 'GET' and path.startswith('/orders?')
    p = path if include_querystring else path.split('?')[0]
    msg = 't' + timestamp + method + p
    msg += (str(recv_window) if recv_window else '') + (json.dumps(body_json) if body_json else '')
    raw_secret = base64.b64decode(SECRET)
    raw_signature = hmac.new(raw_secret, str(msg).encode('utf-8'), hashlib.sha512).digest()
    signature = base64.b64encode(raw_signature)
    headers = {'api-key': API_KEY, 'timestamp': timestamp, 'signature': signature}
    if recv_window:
      headers['receive-window'] = str(recv_window)
  else:
    headers = {}
  req_func = {'GET': requests.get, 'POST': requests.post, 'DELETE': requests.delete}[method]
  resp = req_func(url='https://api.gopax.co.kr' + path, headers=headers, json=body_json)
  return {
    'statusCode': resp.status_code,
    'body': resp.json(),
    'header': dict(resp.headers),
  }


post_orders_req_body = {
  'side': 'buy', 'type': 'limit', 'amount': 1,
  'price': 10000, 'tradingPairName': 'BTC-KRW'
}
print(call(True, 'POST', '/orders', post_orders_req_body, 200))
print(call(True, 'GET', '/orders'))
print(call(True, 'GET', '/orders?includePast=true'))
print(call(True, 'GET', '/trades?limit=1'))
print(call(False, 'GET', '/trading-pairs/BTC-KRW/book?level=1'))
```

</div>
</details>

<br>

* * *

<br>

+ #### Sample JavaScript Source code

<details>
<summary>JavaScript</summary>
<div markdown="1">

```js
const XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
const crypto = require('crypto');

const API_KEY = '<입력하세요>';
const SECRET = '<입력하세요>';

function call(needAuth, method, path, bodyJson = null, recvWindow = null) {
  const bodyStr = bodyJson ? JSON.stringify(bodyJson) : '';
  const http = new XMLHttpRequest();
  const methodInUpperCase = method.toUpperCase();
  http.open(methodInUpperCase, `https://api.gopax.co.kr${path}`, false);
  if (needAuth) {
    const timestamp = new Date().getTime();
    const includeQuerystring = methodInUpperCase === 'GET' && path.startsWith('/orders?');
    const p = includeQuerystring ? path : path.split('?')[0];
    const msg = `t${timestamp}${methodInUpperCase}${p}${recvWindow || ''}${bodyStr}`;
    const rawSecret = Buffer.from(SECRET, 'base64');
    const signature = crypto.createHmac('sha512', rawSecret).update(msg).digest('base64');
    http.setRequestHeader('api-key', API_KEY);
    http.setRequestHeader('timestamp', timestamp);
    http.setRequestHeader('signature', signature);
    if (recvWindow) {
      http.setRequestHeader('receive-window', recvWindow);
    }
  }
  http.send(bodyStr);
  return {
    statusCode: http.status,
    body: JSON.parse(http.responseText),
    header: http.getAllResponseHeaders(),
  };
}

function printAllDepth(json) {
  console.dir(json, { depth: null });
}

const postOrdersReqBody = {
  side: 'buy', type: 'limit', amount: 1,
  price: 10000, tradingPairName: 'BTC-KRW',
};
printAllDepth(call(true, 'POST', '/orders', postOrdersReqBody, 200));
printAllDepth(call(true, 'GET', '/orders'));
printAllDepth(call(true, 'GET', '/orders?includePast=true'));
printAllDepth(call(true, 'GET', '/trades?limit=1'));
printAllDepth(call(false, 'GET', '/trading-pairs/BTC-KRW/book?level=1'));
```

</div>
</details>

<br>

* * *

<br>

+ #### Sample Go lang Source code

<details>
<summary>Go lang</summary>
<div markdown="1">

```go
package main

import (
    "bytes"
    "crypto/hmac"
    "crypto/sha512"
    "encoding/base64"
    "encoding/json"
    "io/ioutil"
    "log"
    "net/http"
    "strconv"
    "strings"
    "time"
)

const (
    apiKey = "<입력하세요>"
    secret = "<입력하세요>"
)

func call(
    needAuth bool, method string, path string,
    body map[string]interface{}, // can be nil
    recvWindow int, // set -1 not to assign
) *map[string]interface{} {
    method = strings.ToUpper(method)
    var bodyBytes []byte = nil
    if body != nil {
        bodyBytes, _ = json.Marshal(body)
    }

    req, _ := http.NewRequest(method, "https://api.gopax.co.kr"+path, bytes.NewBuffer(bodyBytes))

    if needAuth {
        timestamp := strconv.FormatInt(time.Now().UnixNano()/int64(time.Millisecond), 10)
        msg := "t" + timestamp + method
        if method == "GET" && strings.HasPrefix(path, "/orders?") {
            msg += path
        } else {
            msg += strings.Split(path, "?")[0]
        }
        if recvWindow != -1 {
            msg += strconv.Itoa(recvWindow)
        }
        if bodyBytes != nil {
            msg += string(bodyBytes)
        }

        rawSecret, _ := base64.StdEncoding.DecodeString(secret)
        mac := hmac.New(sha512.New, rawSecret)
        mac.Write([]byte(msg))
        rawSignature := mac.Sum(nil)
        signature := base64.StdEncoding.EncodeToString(rawSignature)

        req.Header.Set("api-key", apiKey)
        req.Header.Set("timestamp", timestamp)
        req.Header.Set("signature", signature)
        if recvWindow != -1 {
            req.Header.Set("receive-window", strconv.Itoa(recvWindow))
        }
    }
    resp, err := (&http.Client{}).Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()
    respBodyBytes, _ := ioutil.ReadAll(resp.Body)
    respBody := make(map[string]interface{})
    json.Unmarshal(respBodyBytes, &respBody)

    return &map[string]interface{}{
        "statusCode": resp.StatusCode,
        "body":       respBody,
        "header":     resp.Header,
    }
}

func main() {
    postOrderReqBody := map[string]interface{}{
        "side": "buy", "type": "limit", "amount": 1,
        "price": 10000, "tradingPairName": "BTC-KRW",
    }
    log.Print(*call(true, "POST", "/orders", postOrderReqBody, 200))
    log.Print(*call(true, "GET", "/orders", nil, -1))
    log.Print(*call(true, "GET", "/orders?includePast=true", nil, -1))
    log.Print(*call(true, "GET", "/trades?limit=1", nil, -1))
    log.Print(*call(false, "GET", "/trading-pairs/BTC-KRW/book?level=1", nil, -1))
}
```

</div>
</details>
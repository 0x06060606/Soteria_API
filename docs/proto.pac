function FindProxyForURL(url, host){
  return randomProxy();
}
function randomProxy(){
  switch(Math.floor(Math.random() *2)){
    case 0: return "HTTP 46.4.96.137:3128;"
    case 1: return "SOCKS5 163.53.209.8:6667;"
    case 2: return "SOCKS4 117.102.86.174:4145;"
    case 3: return "HTTPS 119.110.87.18:8080;"
  }
}

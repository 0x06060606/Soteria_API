function FindProxyForURL(url, host){
  return randomProxy();
}
function randomProxy(){
  switch(Math.floor(Math.random()*4)){
    case 0:
      return "PROXY 69.65.65.178:57556; SOCKS 98.143.145.29:62354; SOCKS 186.248.175.152:4145; PROXY 45.204.14.171:80; DIRECT;";
    case 1:
      return "SOCKS 98.143.145.29:62354; SOCKS 186.248.175.152:4145; PROXY 45.204.14.171:80; PROXY 69.65.65.178:57556; DIRECT;";
    case 2:
      return "SOCKS 186.248.175.152:4145; PROXY 45.204.14.171:80; SOCKS 98.143.145.29:62354; PROXY 69.65.65.178:57556; DIRECT;";
    case 3:
      return "PROXY 45.204.14.171:80; PROXY 69.65.65.178:57556; SOCKS 98.143.145.29:62354; SOCKS 186.248.175.152:4145; DIRECT;";
  }
}

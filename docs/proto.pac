function FindProxyForURL(url, host){
  return randomProxy();
}
function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
function randomProxy(){
  switch(Math.floor(Math.random()*4)){
    case 0: return "HTTP 69.65.65.178:57556; SOCKS5 98.143.145.29:62354; SOCKS4 186.248.175.152:4145; HTTPS 45.204.14.171:80;"
    case 1: return "SOCKS5 98.143.145.29:62354; SOCKS4 186.248.175.152:4145; HTTPS 45.204.14.171:80; HTTP 69.65.65.178:57556;"
    case 2: return "SOCKS4 186.248.175.152:4145; HTTPS 45.204.14.171:80; SOCKS5 98.143.145.29:62354; HTTP 69.65.65.178:57556;"
    case 3: return "HTTPS 45.204.14.171:80; HTTP 69.65.65.178:57556; SOCKS5 98.143.145.29:62354; SOCKS4 186.248.175.152:4145;"
  }
}

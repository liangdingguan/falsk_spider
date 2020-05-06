function tacSign(e, t)
{
window.byted_acrawler.init({
    aid: 24,
    dfp: true
});
        var n = "";
        /^http/.test(e) || (/\/toutiao\//.test(e) || (e = "/toutiao" + e),
        e = location.protocol + "//" + location.host + e);
        for (var r in t)
            n += "&" + r + "=" + encodeURIComponent(t[r]);
        e += e.indexOf("?") > -1 ? e.indexOf("&") > -1 ? n : n.slice(1) : "?" + n.slice(1);
        var o = {
            url: e
        }
          , i = window.byted_acrawler.sign ? window.byted_acrawler.sign(o) : "";
        return i

};
var timestamp1 = Date.parse( new Date());
var url='https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=hh&autoload=true&count=20&en_qc=1&cur_tab=1&from=video&pd=video'
var i=tacSign(url,{timestamp:timestamp1})

document.getElementById("demo").innerHTML=url +'&amp'+'timestamp='+ timestamp1+'&_signature='+i














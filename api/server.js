var http = require('http');
var url = require('url');
var SqlString = require('sqlstring');
var mysql = require('mysql');

var server = http.createServer(function (req, res) {
    var url_parts = url.parse(req.url, true);
    var page = req.url;
    var query = url_parts.query;
  
    var con = mysql.createConnection({
      host: "localhost",
      user: "api",
      password: "COMPSTATCUCORRECTHORSEBATTERYSTAPLE",
      database: "compstat"
    });

    con.connect(function(err) {
        if (err) throw err;
    });


    var select_statement = "SELECT * FROM cases WHERE"
    var any_selected = false;

    if (query["date"] != null)
    {
        select_statement += " DateTime=" + query["date"]
        any_selected = true;
    }
    if (query["category"] != null)
    {
        select_statement += " category=" + "\"" + query["category"] + "\""
        any_selected = true;
    }
    if (query["address"] != null)
    {
        select_statement += " address=" + query["address"]
        any_selected = true;
    }

    if (!any_selected)
    {
        select_statement = "SELECT * FROM cases";       
    }

    select_statement += ";"

    var sel_str = select_statement;
    console.log(sel_str);    

    con.query(sel_str, function (err, result, fields) {
        if (err) throw err;
        var j_data = JSON.stringify(result); 
        res.write(j_data);
        res.writeHead(200, {'Content-type': 'application/json'});
        res.end();    
    });
    con.end();
});

server.listen(8080); 

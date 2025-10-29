var term = require('terminal.js');
var path = require('path');
var static = require('node-static');

var fileServer = new static.Server('./');

require('http').createServer(function(request, response) {
    request.addListener('end', function() {
        fileServer.serve(request, response);
    }).resume();
}).listen(process.env.PORT || 8000);

var shell = process.env.SHELL || 'sh';
term.app('./run.py', process.env.PORT || 8000);
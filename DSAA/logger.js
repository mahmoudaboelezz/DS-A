var url ='http://localhost:8080/logger';
function log(message) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    console.log(message);
}
module.exports.log = log;
console.log(module);
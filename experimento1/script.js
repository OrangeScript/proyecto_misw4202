import http from 'k6/http';

import { check, sleep } from 'k6';


export const options = {

  stages: [

    { duration: '30s', target: 20 },

    { duration: '1m30s', target: 1000 },

    { duration: '20s', target: 0 },

  ],

};


export default function () {
  function httpGet(url, params) {
    var res; 
    for (var retries = 3; retries > 0; retries--) {
        res = http.get(url, params)
        if (res.status != 408 && res.status < 500) {
            return res;
        }
    }
    return res;
  
  }
  const res = httpGet('http://127.0.0.1:5001/obtener_deportista', '');

  check(res, { 'status was 200': (r) => r.status == 200 });

  sleep(1);

}
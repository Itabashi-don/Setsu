const mastodon = require("mastodon");
const fs = require("fs");

let mstdn = new mastodon({
    api_url: "https://itabashi.0j0.jp/api/v1/",
    access_token: process.env.token
});

mstdn.post("statuses", {
    status: 'test'
});
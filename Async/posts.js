// let beolvas = async () => {
//     try {
//         const data = await fetch('https://jsonplaceholder.typicode.com/photos');
//         const result = await data.json();
//         let tartalom = document.getElementById('tartalom');
//         for (let i = 0; i < 20; i++) {
//             let kep = document.createElement('img');
//             kep.setAttribute('src', result[i].url);
//             tartalom.appendChild(kep);
//         }
//     } catch (error) {
//         console.log(error.message);
//     }
// };

// beolvas();

// fetch('https://jsonplaceholder.typicode.com/photos')
//     .then(response => response.json())
//     .then(data => {
//         let tartalom = document.getElementById('tartalom');
//         for (let i = 0; i < 20; i++) {
//             let kep = document.createElement('img');
//             kep.setAttribute('src', data[i].url);
//             tartalom.appendChild(kep);
//         }
//     });

let beolvas = async () => {
    try {
        const result = await fetch('https://api.github.com/users');
        const data = await result.json();
        return data;
    } catch (error) {
        console.log(error.message);
    }
};

let osszerak = async () => {
    try {
        let data = await beolvas();
        console.log(data);
        let tartalom = document.getElementById('tartalom');
        for (let i = 0; i < data.length; i++) {
            let nev = document.createElement('div');
            let loginszoveg = data[i].login;
            let loginNode = document.createTextNode(loginszoveg);
            nev.appendChild(loginNode);

            let nodeid = document.createElement('div');
            let nodeSzoveg = data[i].node_id;
            let nodeNode = document.createTextNode(nodeSzoveg);
            nodeid.appendChild(nodeNode);

            let avatarurl = document.createElement('div');
            let avatarSzoveg = data[i].avatar_url;
            let avatarNode = document.createTextNode(avatarSzoveg);
            avatarurl.appendChild(avatarNode);

            let url = document.createElement('div');
            let urlSzoveg = data[i].url;
            let urlNode = document.createTextNode(urlSzoveg);
            url.appendChild(urlNode);

            let html_url = document.createElement('div');
            let html_urlSzoveg = data[i].html_url;
            let html_urlNode = document.createTextNode(html_urlSzoveg);
            html_url.appendChild(html_urlNode);

            let followers_url = document.createElement('div');
            let followers_urlSzoveg = data[i].followers_url;
            let followers_urlNode = document.createTextNode(followers_urlSzoveg);
            followers_url.appendChild(followers_urlNode);

            let gists_url = document.createElement('div');
            let gists_urlSzoveg = data[i].gists_url;
            let gists_urlNode = document.createTextNode(gists_urlSzoveg);
            gists_url.appendChild(gists_urlNode);

            
            let starred_url = document.createElement('div');
            let starred_urlSzoveg = data[i].starred_url;
            let starred_urlNode = document.createTextNode(starred_urlSzoveg);
            starred_url.appendChild(starred_urlNode);

            let subscriptions_url = document.createElement('div');
            let subscriptions_urlSzoveg = data[i].subscriptions_url;
            let subscriptions_urlNode = document.createTextNode(subscriptions_urlSzoveg);
            subscriptions_url.appendChild(subscriptions_urlNode);
            
            let organizations_url = document.createElement('div');
            let organizations_urlSzoveg = data[i].organizations_url;
            let organizations_urlNode = document.createTextNode(organizations_urlSzoveg);
            organizations_url.appendChild(organizations_urlNode);

            
            let repos_url = document.createElement('div');
            let repos_urlSzoveg = data[i].repos_url;
            let repos_urlNode = document.createTextNode(repos_urlSzoveg);
            repos_url.appendChild(repos_urlNode);

            let events_url = document.createElement('div');
            let events_urlSzoveg = data[i].events_url;
            let events_urlNode = document.createTextNode(events_urlSzoveg);
            events_url.appendChild(events_urlNode);

            let received_events_url = document.createElement('div');
            let received_events_urlSzoveg = data[i].received_events_url;
            let received_events_urlNode = document.createTextNode(received_events_urlSzoveg);
            received_events_url.appendChild(received_events_urlNode);

            let type = document.createElement('div');
            let typeSzoveg = data[i].type;
            let typeNode = document.createTextNode(typeSzoveg);
            type.appendChild(typeNode);

            let site_admin = document.createElement('div');
            let site_adminSzoveg = data[i].site_admin;
            let site_adminNode = document.createTextNode(site_adminSzoveg);
            site_admin.appendChild(site_adminNode);

            let tarto = document.createElement('div');
            tarto.setAttribute('class', 'container');
            tarto.appendChild(nev);
            tarto.appendChild(nodeid);
            tarto.appendChild(avatarurl);
            tarto.appendChild(url);
            tarto.appendChild(html_url);
            tarto.appendChild(followers_url);
            tarto.appendChild(gists_url);
            tarto.appendChild(starred_url);
            tarto.appendChild(subscriptions_url);
            tarto.appendChild(organizations_url);
            tarto.appendChild(repos_url);
            tarto.appendChild(events_url);
            tarto.appendChild(received_events_url);
            tarto.appendChild(type);
            tarto.appendChild(site_admin);



            tartalom.appendChild(tarto);
        }
    } catch (error) {
        console.log(error.message);
    }

};

osszerak();
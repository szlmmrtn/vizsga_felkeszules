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
        const result = await fetch('https://jsonplaceholder.typicode.com/posts');
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
        for (let i = 0; i < 9; i++) {
            let cim = document.createElement('h1');
            let cimSzoveg = data[i].title;
            let cimNode = document.createTextNode(cimSzoveg);
            cim.appendChild(cimNode);

            let tart = document.createElement('div');
            let tartSzoveg = data[i].body;
            let tartNode = document.createTextNode(tartSzoveg);
            tart.appendChild(tartNode);

            let tarto = document.createElement('div');
            tarto.setAttribute('class', 'container');
            tarto.appendChild(cim);
            tarto.appendChild(tart);

            tartalom.appendChild(tarto);
        }
    } catch (error) {
        console.log(error.message);
    }

};


osszerak();
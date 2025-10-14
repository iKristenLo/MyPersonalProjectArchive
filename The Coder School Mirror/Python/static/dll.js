document.getElementById("scanbt").addEventListener("click", function() {
    document.getElementById("result").innerHTML = "<p class='loading'>Scanning... Please wait.</p>";
    fetch("/endpoint")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerHTML = "<p class='error'>Error: " + data.error + "</p>";
            } else {
                let resultDiv = document.getElementById("result");
                resultDiv.innerHTML = "";
                let results = data.dllresults;
                if (!results || results.length === 0) {
                    resultDiv.innerHTML = "<p>No suspicious DLLs found.</p>";
                } else {
                    let table = document.createElement("table");
                    let header = document.createElement("tr");
                    ["Process Name", "PID", "DLL Name", "DLL Path", "System DLL Path", "Score"].forEach(function(text) {
                        let th = document.createElement("th");
                        th.textContent = text;
                        header.appendChild(th);
                    });
                    table.appendChild(header);
                    results.forEach(function(item) {
                        let row = document.createElement("tr");

                        let cell1 = document.createElement("td");
                        cell1.textContent = item.name;
                        row.appendChild(cell1);

                        let cell2 = document.createElement("td");
                        cell2.textContent = item.pid;
                        row.appendChild(cell2);

                        let cell3 = document.createElement("td");
                        cell3.textContent = item.dll;
                        row.appendChild(cell3);

                        let cell4 = document.createElement("td");
                        let pathbox = document.createElement("div");
                        pathbox.classList.add("dllbox");
                        pathbox.textContent = item.path;
                        cell4.appendChild(pathbox);
                        row.appendChild(cell4);

                        let cell5 = document.createElement("td");
                        cell5.textContent = item.syspath;
                        row.appendChild(cell5);

                        let cell6 = document.createElement("td");
                        cell6.textContent = item.dlscore;
                        row.appendChild(cell6);

                        table.appendChild(row);
                    });
                    resultDiv.appendChild(table);
                }
            }
        })
        .catch(error => {
            document.getElementById("result").innerHTML = "<p class='error'>Error: " + error + "</p>";
        });
});

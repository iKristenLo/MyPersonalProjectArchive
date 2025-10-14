document.getElementById('fileForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const resultDiv = document.getElementById('result');
    
    try {
        resultDiv.innerHTML = '<div class="loading">Analyzing file...</div>';
        
        const response = await fetch('/sigcheck', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }

        let verdiict = "";
        const verdtext = data.verdict.toLowerCase();
        if(verdtext.includes("safe")){
            verdiict = "valid";
        } else if (verdtext.includes("sus")){
            verdiict = "possible";
        } else if (verdtext.includes("virus")){
            verdiict = "invalid";
        }

        resultDiv.innerHTML = `
            <div class="result-card">
                <h3>Analysis Results</h3>
                <div class="result-item">
                    <span class="label">SHA-256 Hash:</span>
                    <span class="value">${data.hash}</span>
                </div>
                <div class="result-item">
                    <span class="label">Verdict:</span>
                    <span class="value ${verdiict}">
                        ${data.verdict}
                    </span>
                </div>
            </div>`;
        
    } catch (error) {
        resultDiv.innerHTML = `
            <div class="error">
                Error: ${error.message}
            </div>`;
    }
});
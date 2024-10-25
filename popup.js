document.getElementById("runAI").addEventListener("click", async () => {
  const imageData = getImageData();
  const response = await fetch('http://localhost:5000/infer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image_data: imageData })
  });
  const result = await response.json();
  console.log("Inference Result:", result);
});

function getImageData() {
  // Logic to extract image data from the webpage (optional).
}

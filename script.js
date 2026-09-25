const langBtn = document.getElementById("langBtn");
const searchBtn = document.getElementById("searchBtn");

langBtn.addEventListener("click", function () {
  alert("English version जल्द उपलब्ध होगी।");
});

searchBtn.addEventListener("click", function () {
  const query = prompt("आप कौन सी खबर खोज रहे हैं?");

  if (!query) {
    return;
  }

  const text = document.body.innerText.toLowerCase();

  if (text.includes(query.toLowerCase())) {
    alert("आपकी खोज से संबंधित सामग्री वेबसाइट पर मौजूद है।");
  } else {
    alert("इस समय इस विषय की खबर नहीं मिली।");
  }
});

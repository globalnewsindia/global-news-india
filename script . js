const data = {
  world: [
    ["विश्व", "अंतरराष्ट्रीय समाचारों के लिए आपका नया सेक्शन", "यहाँ सत्यापित और मौलिक समाचार सारांश प्रकाशित किए जाएँगे।"],
    ["World", "Global News Updates", "English-language global news will appear here."]
  ],
  india: [
    ["भारत", "भारत की ताज़ा और महत्वपूर्ण खबरें", "विश्वसनीय स्रोतों से जानकारी लेकर अपनी भाषा में समाचार तैयार किए जाएँगे।"],
    ["India", "India News", "Verified India news will appear here."]
  ],
  business: [
    ["बिज़नेस", "बिज़नेस और अर्थव्यवस्था की खबरें", "मार्केट, कंपनियों और अर्थव्यवस्था से जुड़ी खबरें।"]
  ],
  tech: [
    ["टेक्नोलॉजी", "टेक की दुनिया की नई खबरें", "AI, मोबाइल, इंटरनेट और डिजिटल दुनिया की खबरें।"]
  ]
};

function render(id, items) {
  const box = document.getElementById(id + "Cards");
  if (!box) return;

  box.innerHTML = items.map(item =>
    `<article class="card">
      <div class="category">${item[0]}</div>
      <h3>${item[1]}</h3>
      <p>${item[2]}</p>
    </article>`
  ).join("");
}

render("world", data.world);
render("india", data.india);
render("business", data.business);
render("tech", data.tech);

let english = false;

document.getElementById("langBtn").onclick = () => {
  english = !english;

  document.documentElement.lang = english ? "en" : "hi";

  document.getElementById("langBtn").textContent =
    english ? "हिंदी" : "English";

  document.getElementById("headline").textContent =
    english
      ? "Top news from India and around the world"
      : "दुनिया और भारत की प्रमुख खबरें एक ही जगह";

  document.getElementById("summary").textContent =
    english
      ? "Your new bilingual news website homepage."
      : "यह आपकी नई द्विभाषी न्यूज़ वेबसाइट का शुरुआती होमपेज है।";
};

document.getElementById("searchBtn").onclick = () => {
  alert("Search feature अगले चरण में जोड़ा जाएगा।");
};

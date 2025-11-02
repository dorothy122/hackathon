const SHEET_ID = "1uwzjj0GZYSWBMtONWtTQBac__r4024xXKiH10wKMkAI"
const GEMINI_KEY = "AIzaSyCNVp1wXMcL1Fmn7P3dwIz4G9zlNEGZu74"
const API_KEY = "AIzaSyCfz4_k-Rye8hMCu5s139lX6RUxfqROr-g"

async function getLastRecord() {
  const url = `https://sheets.googleapis.com/v4/spreadsheets/${SHEET_ID}/values/Sheet1?key=${API_KEY}`;
  const res = await fetch(url);
  const data = await res.json();

  const rows = data.values;
  const headers = rows[0];
  const values = rows[rows.length - 1];

  const record = {};
  headers.forEach((h, i) => {
    record[h] = values[i];
  });

  return record;
}

function calculate(record) {
  let twins = false;
  let married = false;
  let rich = true;
  let moveCountries = false;

  if (record.Gender === "F" && Number(record.Height) > 164) {
    twins = true;
  } else if (Number(record.Height) > 180) {
    married = true;
  }

  const careers = {
    january: "an athlete",
    february: "an artist",
    march: "a pilot",
    april: "a dictator",
    may: "a politician",
    june: "a CEO",
    july: "a bricklayer",
    august: "a hairdresser",
    september: "an academic",
    october: "a lawyer",
    november: "a serial killer",
    december: "a dentist",
  };
  const career = careers[record.BirthMonth.toLowerCase()];

  if (record.Drive === "No" || record.Glasses === "Yes") {
    rich = true;
  }

  if (record.Tongue === "Yes") {
    moveCountries = true;
  }

  let rememberedFor = "";
  const firstInitial = record.FirstName.toLowerCase().charCodeAt(0) - "a".charCodeAt(0) + 1;

  if (firstInitial < 5) rememberedFor = "winning an award";
  else if (firstInitial < 9) rememberedFor = "doing something embarrassing";
  else if (firstInitial < 13) rememberedFor = "always being kind";
  else if (firstInitial < 17) rememberedFor = "being the best at your job";
  else if (firstInitial < 21) rememberedFor = "being intelligent";
  else if (firstInitial < 25) rememberedFor = "being forgetful";
  else rememberedFor = "that one thing you did in Vegas";

  return { twins, married, rich, moveCountries, career, rememberedFor };
}


async function generateParagraph(record, calc) {
  const prompt = `Create a short paragraph in future tense second person detailing the legacy of a person based on:
  name: ${record.FirstName} ${record.LastName},
  career: ${calc.career},
  likely to get married: ${calc.married},
  likely to have twins: ${calc.twins},
  likely to be rich: ${calc.rich},
  being remembered for: ${calc.rememberedFor}` + "add something unique";

    const res = await fetch(
    "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=" + GEMINI_KEY,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
      }),
    }
  );



  const data = await res.json();
  console.log("Gemini raw response:", data); 
  const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text;
  console.log(generatedText); 

  return generatedText || "No response";
}


// Main
async function loadResults() {
  try {
    const record = await getLastRecord();
    const calc = calculate(record);
    const paragraph = await generateParagraph(record, calc);
    document.getElementById("results").innerText = paragraph;
  } catch (err) {
    console.error(err);
    document.getElementById("results").innerText = "Error loading results.";
  }
}

window.onload = loadResults;




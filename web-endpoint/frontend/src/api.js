export async function generateText(prompt) {
  const res = await fetch("https://llm.strangebit.io:/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: prompt })
  });

  return await res.json();
}

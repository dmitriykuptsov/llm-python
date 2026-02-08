<script setup>
import { ref } from "vue"
import { generateText } from "./api"

const prompt = ref("")
const output = ref("")
const loading = ref(false)

async function runAgent() {
  loading.value = true
  const res = await generateText(prompt.value)
  output.value = res.response
  loading.value = false
}
</script>

<template>
  <div class="page">
    <h1>VPLS LLM help agent</h1>

    <textarea
      v-model="prompt"
      placeholder="Enter your prompt..."
      rows="6"
    />

    <button @click="runAgent" :disabled="loading" class="btn-primary">
      {{ loading ? "Thinking..." : "Run Agent" }}
    </button>

    <pre v-if="output">{{ output }}</pre>
  </div>
</template>

<style>

body {
  font-family: Inter, system-ui, sans-serif;
  color: #111827;
}
.card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}
.btn-primary {
  background: #4F46E5;
  color: white;
  padding: 10px 18px;
  border-radius: 10px;
  font-weight: 500;
}
.btn-primary:hover {
  background: #4338CA;
}
.btn-secondary {
  background: #F3F4F6;
  color: #111827;
}
input, select {
  border: 1px solid #E5E7EB;
  border-radius: 10px;
  padding: 10px 12px;
}
input:focus {
  outline: none;
  border-color: #4F46E5;
  box-shadow: 0 0 0 3px rgba(79,70,229,0.15);
}
.page {
  width: 100%;
  min-height: 100vh;
  padding: 2rem;
}
textarea {
  width: 100%;
  margin-bottom: 1rem;
  border: 1px solid #E5E7EB;
  border-radius: 10px;
  padding: 10px 12px;
  font-family: Inter, system-ui, sans-serif;
  color: #111827;
}
button {
  padding: 0.5rem 1rem;
}
pre {
  background: #111;
  color: #0f0;
  padding: 1rem;
  white-space: pre-wrap;
}
h1 {
  color: aqua;
}
</style>

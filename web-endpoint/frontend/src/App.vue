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
  <div class="container">
    <h1>Custom LLM Agent</h1>

    <textarea
      v-model="prompt"
      placeholder="Enter your prompt..."
      rows="6"
    />

    <button @click="runAgent" :disabled="loading">
      {{ loading ? "Thinking..." : "Run Agent" }}
    </button>

    <pre v-if="output">{{ output }}</pre>
  </div>
</template>

<style>
.container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
  font-family: sans-serif;
}
textarea {
  width: 100%;
  margin-bottom: 1rem;
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
</style>

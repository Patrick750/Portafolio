<template>
  <Navbar />
  <main>
    <Hero />
    <Skills />
    <Projects />
    <Footer />
  </main>
</template>

<script setup>
import Navbar   from './Navbar.vue'
import Hero     from './Hero.vue'
import Skills   from './Skills.vue'
import Projects from './Projects.vue'
import Footer   from './Footer.vue'
</script>

<style scoped>
main {
  padding-top: 0;
}
</style>

<script setup>
import Navbar   from './components/Navbar.vue'
import Hero     from './components/Hero.vue'
import Skills   from './components/Skills.vue'
import Projects from './components/Projects.vue'
import Footer   from './components/Footer.vue'
</script>

<template>
  <Navbar />
  <main>
    <Hero />
    <Skills />
    <Projects />
    <Footer />
  </main>
</template>

<style>
main {
  /* Offset for fixed navbar */
  padding-top: 0;
}
</style>

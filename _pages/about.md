---
layout: minimal
nav: about
title: "About"
permalink: /
description: "Postdoctoral researcher — machine learning & physics, AI safety."
redirect_from:
  - /about/
  - /about.html
---

<p class="note">The site is under construction — sorry for the (temporarily) limited information.</p>

<section class="intro">
  <div class="portrait">
    <img src="/images/jv_s.jpg" alt="Jakub Vrabel">
    <ul class="socials">
      <li><a href="https://scholar.google.com/citations?user=MCnlDZUAAAAJ&hl" target="_blank" rel="noopener">scholar</a></li>
      <li><a href="https://github.com/jvrabel" target="_blank" rel="noopener">github</a></li>
      <li><a href="https://www.linkedin.com/in/jakub-vrabel" target="_blank" rel="noopener">linkedin</a></li>
      <li><a href="https://twitter.com/VrabelJakub" target="_blank" rel="noopener">twitter</a></li>
    </ul>
  </div>
  <div>
    <p>I am a postdoctoral researcher at <a href="https://www.ceitec.eu/" target="_blank" rel="noopener">CEITEC</a>
    with interests in technical AI safety, security, and the science of deep learning. I hold a PhD in applied
    physics and have worked on interpretable machine learning for spectroscopy as well as foundational aspects of
    deep learning. I also collaborate with <a href="https://www.kasl.ai/" target="_blank" rel="noopener">KASL</a>
    and was previously a visiting Ph.D. student at the University of Cambridge, advised by David Krueger.</p>
  </div>
</section>

<p>My current research focuses on foundational topics in machine learning — loss-landscape geometry, parameter-space
symmetries, mode connectivity, and overparameterization — with the broader aim of advancing AI security and safety.
I combine empirical and theoretical approaches, often grounded in physics, to better understand deep learning and
improve its interpretability and robustness.</p>

<p class="muted">When I'm not busy with ML experiments, you can find me bouldering or cycling. I also enjoy hiking,
playing guitar, and reading physics books from my vast collection.</p>

<h2>News</h2>
<ul class="news">
  <li><span class="date">Jul 2026</span>Joining <a href="https://www.cst.cam.ac.uk/" target="_blank" rel="noopener">CST</a>,
    University of Cambridge, as a postdoctoral research associate.</li>
  <li><span class="date">Oct 2025</span>Gave a talk on Mode Connectivity for AI Security &amp; Safety at the
    <a href="https://www.oaisi.org/" target="_blank" rel="noopener">Oxford AI Safety Initiative</a>'s technical roundtable seminar.</li>
  <li><span class="date">Jul 2025</span>Joining the Artificial Intelligence Governance Initiative (AIGI) at the
    University of Oxford as a Visiting Research Fellow for three months, working on automated interpretability (with Fazl Barez).</li>
  <li><span class="date">Jan 2025</span>Input space mode connectivity was accepted to
    <a href="https://openreview.net/forum?id=3qeOy7HwUT" target="_blank" rel="noopener">ICLR 2025</a>.</li>
  <li><span class="date">Oct 2024</span>Input space mode connectivity accepted for an
    <a href="https://neurips.cc/virtual/2024/workshop/84741#collapse-sl-109173" target="_blank" rel="noopener">oral presentation</a> at
    <a href="https://scienceofdlworkshop.github.io/" target="_blank" rel="noopener">SciForDL</a> at NeurIPS 2024.</li>
  <li><span class="date">Aug 2024</span>Attending the <a href="https://iaifi.org/phd-summer-school.html" target="_blank" rel="noopener">IAIFI summer school</a>
    and <a href="https://iaifi.org/summer-workshop.html" target="_blank" rel="noopener">workshop</a> at MIT, giving a talk on input space mode connectivity.</li>
  <li><span class="date">Jun 2024</span>Visiting <a href="https://www.kasl.ai/" target="_blank" rel="noopener">KASL</a> ⊂
    <a href="https://mlg.eng.cam.ac.uk/" target="_blank" rel="noopener">CBL</a>, University of Cambridge, for four months.</li>
  <li><span class="date">May 2024</span>At the <a href="https://indico.ictp.it/event/10478" target="_blank" rel="noopener">Youth in High Dimensions</a>
    workshop at ICTP in Trieste, Italy.</li>
</ul>

<h2>Research interests</h2>
<ul>
  <li>Machine learning foundations
    <ul>
      <li>overparametrization, double descent, NTK</li>
      <li>loss-landscape symmetries, mode connectivity</li>
      <li>sparsity, lottery tickets</li>
    </ul>
  </li>
  <li>ANN interpretability (for spectroscopic data)
    <ul>
      <li>feature visualization, optimal manifold</li>
      <li>sparsity for (mechanistic) interpretability</li>
      <li>custom loss penalization</li>
    </ul>
  </li>
  <li>AI safety
    <ul>
      <li>LLM jailbreaking (defenses)</li>
    </ul>
  </li>
</ul>

<h2>Current projects</h2>

<div class="project">
  <img src="/images/mode_connectivity.png" alt="">
  <div class="body">
    <h3>Input space mode connectivity</h3>
    <p>We generalized the concept of loss-landscape mode connectivity to the input space of deep neural networks.</p>
    <div class="links">
      <a href="https://openreview.net/forum?id=3qeOy7HwUT" target="_blank" rel="noopener">ICLR</a><span class="sep">|</span>
      <a href="https://arxiv.org/abs/2409.05800" target="_blank" rel="noopener">arXiv</a><span class="sep">|</span>
      <a href="https://neurips.cc/virtual/2024/workshop/84741#collapse-sl-109173" target="_blank" rel="noopener">Talk (D. Krueger)</a>
    </div>
  </div>
</div>

<div class="project">
  <img src="/images/sparsity_custom.png" alt="">
  <div class="body">
    <h3>Sparse, interpretable ANNs for spectroscopic data</h3>
    <p>We study custom loss penalization for MLPs that leads to interpretable and spectroscopically relevant weights in the first layer.</p>
    <div class="links">
      <a href="https://github.com/JVrabel/custom_loss_sparsity" target="_blank" rel="noopener">Code</a>
    </div>
  </div>
</div>

<div class="project">
  <img src="/images/double_descent.png" alt="">
  <div class="body">
    <h3>Lottery tickets vs. double descent</h3>
    <p>A solo project studying intrinsic limitations of lottery-ticket performance as it depends on the initial effective complexity.</p>
  </div>
</div>

<h2>Selected past projects</h2>

<div class="project">
  <img src="/images/spectra_transfer.png" alt="">
  <div class="body">
    <h3>Spectral library transfer between two LIBS systems</h3>
    <p>We used a composed model (VAE + MLP) to transfer spectra between two distinct instruments.</p>
    <div class="links">
      <a href="https://doi.org/10.1039/D2JA00406B" target="_blank" rel="noopener">Paper</a><span class="sep">|</span>
      <a href="https://github.com/LIBS-ML-team/libs-transfer-library" target="_blank" rel="noopener">Code</a>
    </div>
  </div>
</div>

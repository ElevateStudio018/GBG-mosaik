(function () {
  "use strict";

  // Mobilmeny under sidhuvudet.
  var btn = document.getElementById("menuBtn");
  var menu = document.getElementById("menu");
  if (btn && menu) {
    var setOpen = function (open) {
      menu.hidden = !open;
      btn.setAttribute("aria-expanded", String(open));
      btn.setAttribute("aria-label", open ? "Stäng menyn" : "Meny");
    };
    btn.addEventListener("click", function () { setOpen(menu.hidden); });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menu.hidden) { setOpen(false); btn.focus(); }
    });
  }

  // Undermenyer: klick på knappen öppnar, klick utanför eller Esc stänger.
  var subs = document.querySelectorAll(".has-sub");
  function closeSubs(except) {
    subs.forEach(function (li) {
      if (li === except) return;
      li.classList.remove("open");
      li.querySelector(".sub-btn").setAttribute("aria-expanded", "false");
    });
  }
  subs.forEach(function (li) {
    var b = li.querySelector(".sub-btn");
    b.addEventListener("click", function () {
      var open = !li.classList.contains("open");
      closeSubs(li);
      li.classList.toggle("open", open);
      b.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".has-sub")) closeSubs(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeSubs(); });

  var head = document.querySelector(".head");
  function onScroll() { if (head) head.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });

  var calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Bildspelet i toppen på startsidan (samma bilder som på den gamla hemsidan).
  var slides = document.querySelectorAll(".slides .slide");
  if (slides.length > 1 && !calm) {
    var cur = 0;
    setInterval(function () {
      if (document.hidden) return;
      slides[cur].classList.remove("on");
      cur = (cur + 1) % slides.length;
      slides[cur].classList.add("on");
    }, 6500);
  }

  // Mjuk inflygning av sektionernas innehåll.
  if ("IntersectionObserver" in window && !calm) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".sec .sec-head, .cards > li, .steps > li, .split > *, .svcs > li, .finishes > li, .mat, .prod, .doc-group")
      .forEach(function (el) { el.classList.add("reveal"); io.observe(el); });
  }

  // Filter för färgkollektionen.
  document.querySelectorAll(".chips").forEach(function (group) {
    var list = group.nextElementSibling;
    group.addEventListener("click", function (e) {
      var chip = e.target.closest(".chip");
      if (!chip) return;
      var f = chip.getAttribute("data-filter");
      group.querySelectorAll(".chip").forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
      list.querySelectorAll("li").forEach(function (li) { li.hidden = f !== "*" && li.getAttribute("data-group") !== f; });
    });
  });

  // Bildvisning för gallerier och kulörer.
  var lb = document.getElementById("lb");
  if (lb && typeof lb.showModal === "function") {
    var lbImg = document.getElementById("lb-img");
    var lbCap = document.getElementById("lb-cap");
    var lbOrder = document.getElementById("lb-order");
    var set = [], idx = 0;
    var show = function (i) {
      idx = (i + set.length) % set.length;
      var el = set[idx];
      lbImg.src = el.getAttribute("data-lb");
      lbImg.alt = el.getAttribute("data-caption") || "";
      lbCap.textContent = el.getAttribute("data-caption") || "";
      var code = el.getAttribute("data-code");
      lbOrder.hidden = !code;
      if (code) lbOrder.href = "kontakt.html?typ=" + encodeURIComponent("Beställ prover") + "&kulor=" + encodeURIComponent(code) + "#offert";
      lb.querySelectorAll(".lb-nav").forEach(function (n) { n.hidden = set.length < 2; });
    };
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-lb]");
      if (!t) return;
      var scope = t.closest("ul");
      set = Array.prototype.filter.call(scope.querySelectorAll("[data-lb]"), function (el) { return !el.closest("li[hidden]"); });
      show(set.indexOf(t));
      lb.showModal();
    });
    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.closest("[data-lb-close]")) lb.close();
      var step = e.target.closest("[data-lb-step]");
      if (step) show(idx + Number(step.getAttribute("data-lb-step")));
    });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") show(idx + 1);
      if (e.key === "ArrowLeft") show(idx - 1);
    });
  }

  // Formuläret: kontrolleras här, skickas via FormSubmit och ersätts sedan av ett tack.
  var form = document.getElementById("qform");
  if (!form) return;
  var done = document.getElementById("qdone");
  var sendErr = document.getElementById("send-err");
  var f = {};
  ["namn", "foretag", "tel", "epost", "typ", "kulor", "adr", "besk", "web"].forEach(function (k) { f[k] = document.getElementById("f-" + k); });

  // "Begär offert" eller "Beställ prov" på en annan sida kommer hit med ?typ=…&kulor=…
  var params = new URLSearchParams(location.search);
  var typ = params.get("typ");
  if (typ) for (var i = 0; i < f.typ.options.length; i++) if (f.typ.options[i].text === typ) f.typ.selectedIndex = i;
  if (params.get("kulor")) f.kulor.value = params.get("kulor");
  var adrField = document.getElementById("adr-field");
  function toggleAdr() { adrField.hidden = f.typ.value !== "Beställ prover"; }
  f.typ.addEventListener("change", toggleAdr);
  toggleAdr();

  function mark(key, input, bad) {
    document.getElementById("e-" + key).hidden = !bad;
    input.setAttribute("aria-invalid", bad ? "true" : "false");
    if (bad) input.setAttribute("aria-describedby", "e-" + key); else input.removeAttribute("aria-describedby");
  }
  function validate() {
    var bad = [];
    var tel = f.tel.value.trim(), ep = f.epost.value.trim();
    var namnBad = !f.namn.value.trim();
    var contactBad = !tel && !ep;
    var epBad = !!ep && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(ep);
    mark("namn", f.namn, namnBad); if (namnBad) bad.push(f.namn);
    mark("tel", f.tel, contactBad); if (contactBad) bad.push(f.tel);
    mark("epost", f.epost, epBad); if (epBad) bad.push(f.epost);
    return bad;
  }
  form.addEventListener("input", function (e) {
    if (e.target.getAttribute("aria-invalid") === "true" || e.target === f.tel || e.target === f.epost) validate();
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var bad = validate();
    if (bad.length) { bad[0].focus(); return; }
    var submit = form.querySelector("button[type=submit]");
    submit.disabled = true;
    submit.textContent = "Skickar …";
    sendErr.hidden = true;
    var v = function (el) { return el.value.trim() || "–"; };
    var payload = {
      _subject: (f.typ.value || "Förfrågan") + " från hemsidan – " + f.namn.value.trim(),
      _template: "table",
      _captcha: "false",
      _honey: f.web.value,
      Namn: v(f.namn),
      "Företag": v(f.foretag),
      Telefon: v(f.tel),
      "E-post": v(f.epost),
      "Gäller": f.typ.value || "–",
      "Kulörer / artiklar": v(f.kulor),
      "Adress för prover": adrField.hidden ? "–" : v(f.adr),
      Beskrivning: v(f.besk)
    };
    if (f.epost.value.trim()) payload._replyto = f.epost.value.trim();
    fetch(form.getAttribute("data-endpoint"), {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(payload)
    }).then(function (r) {
      return r.json().catch(function () { return null; }).then(function (j) {
        if (!r.ok || !j || String(j.success) !== "true") throw new Error("not sent");
      });
    }).then(function () {
      form.reset();
      form.hidden = true;
      done.hidden = false;
      done.focus();
    }).catch(function () {
      sendErr.hidden = false;
    }).then(function () {
      submit.disabled = false;
      submit.textContent = "Skicka";
    });
  });

  document.getElementById("qagain").addEventListener("click", function () {
    done.hidden = true;
    form.hidden = false;
    toggleAdr();
    f.namn.focus();
  });
})();

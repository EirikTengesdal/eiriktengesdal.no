/**
 * Copyright 2019 Google LLC.
 * SPDX-License-Identifier: Apache-2.0
 */
(()=>{window.matchMedia("(prefers-color-scheme)").media;const e=document.querySelector("dark-mode-toggle"),t=document.querySelectorAll('link[rel="manifest"]'),r=document.querySelectorAll('link[rel="icon"]'),o=document.querySelector('meta[name="theme-color"]'),c=e=>{const c="dark"===e.detail.colorScheme;t.forEach(e=>{e.href=c?e.dataset.hrefDark:e.dataset.hrefLight}),r.forEach(e=>{e.href=c?e.dataset.hrefDark:e.dataset.hrefLight}),o.content=c?"black":"white"};document.addEventListener("colorschemechange",c),c({detail:{colorScheme:e.mode}})})();
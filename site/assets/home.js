import { Bit, bitName, negateBit } from "./engine/bit-machine.js";

const control = document.querySelector("[data-hero-bit]");
const label = document.querySelector("[data-hero-bit-label]");
let value = Bit.LOW;

function render() {
  const name = bitName(value);
  control.dataset.value = name;
  control.setAttribute("aria-label", `Bit is ${name}. Activate to negate it.`);
  label.textContent = name;
}

control?.addEventListener("click", () => {
  value = negateBit(value);
  render();
});

render();

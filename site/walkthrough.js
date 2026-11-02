// 教学示例只切换浏览器内已保存的文字，不调用模型或收集输入。
const data = JSON.parse(document.getElementById('example-data').textContent);
const buttons = [...document.querySelectorAll('[data-step]')];
function select(index) {
  buttons.forEach((button, i) => { button.setAttribute('aria-selected', String(i === index)); button.tabIndex = i === index ? 0 : -1; });
  document.getElementById('example-code').textContent = data.codes[index];
  document.getElementById('example-explanation').textContent = data.texts[index];
  document.getElementById('example-panel').setAttribute('aria-labelledby', buttons[index].id);
}
buttons.forEach((button, index) => {
  button.addEventListener('click', () => select(index));
  button.addEventListener('keydown', event => {
    let next = index;
    if (event.key === 'ArrowRight') next = (index + 1) % buttons.length;
    else if (event.key === 'ArrowLeft') next = (index + buttons.length - 1) % buttons.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = buttons.length - 1;
    else return;
    event.preventDefault(); select(next); buttons[next].focus();
  });
});

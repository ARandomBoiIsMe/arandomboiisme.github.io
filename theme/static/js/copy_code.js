document.addEventListener('click', function(e) {
    if (e.target.closest('pre')) {
      const pre = e.target.closest('pre');
      const code = pre.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {
        const button = pre.querySelector('::after');
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.textContent = 'Copy';
        }, 2000);
      });
    }
  });
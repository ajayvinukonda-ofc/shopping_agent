const checkProduct = async () => {
  const name = document.getElementById("productName").value;
  const res = await fetch(`/check?name=${name}`);
  const data = await res.json();
  document.getElementById("responseBox").textContent = JSON.stringify(data, null, 2);
};

const buyProduct = async () => {
  const name = document.getElementById("productName").value;
  const res = await fetch("/buy", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
  const data = await res.json();
  document.getElementById("responseBox").textContent = JSON.stringify(data, null, 2);
};

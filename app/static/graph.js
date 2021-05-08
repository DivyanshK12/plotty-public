window.onload = async () => {
  const { datesData, users, fullData } = await getdata();
  let datasets = [];
  for (let user of users) {
    datasets.push({
      label: user,
      data: fullData[user],
      borderColor: getRandomColor(),
      fill: false,
    });
  }
  charter(datesData, datasets);
};

function charter(datesData, datasets) {
  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: datesData,
      datasets: datasets,
    },
  });
  myChart.update();
}
function getRandomColor() {
  let letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  console.log(color);
  return color;
}
async function getdata() {
  let root = location.href;
  let datesData = await fetch(`${root}/api/getdates`);
  datesData = await datesData.json();
  datesData.sort();
  let users = await fetch(`${root}/api/getusers`);
  users = await users.json();

  let fullData = await fetch(`${root}/api/getdata`);
  fullData = await fullData.json();
  return { datesData, users, fullData };
}

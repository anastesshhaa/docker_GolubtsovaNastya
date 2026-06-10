const fs = require("fs");
const { parse } = require("csv-parse/sync");
const text = fs.readFileSync("/data/data.csv", "utf-8");
const books = parse(text, {
    columns: true
});

let totalWhimsy = 0;
let totalAngst = 0;

for (const book of books) {
    totalWhimsy += Number(book.BOOK_WHIMSINESS_LEVEL);
    totalAngst += Number(book.BOOK_ANGST_LEVEL);
}

const averageWhimsy = totalWhimsy / books.length;
const averageAngst = totalAngst / books.length;
const html = `
<html>
<head>
    <title>Books Report</title>
</head>
<body>
    <h1>Books Report</h1>

    <p>Number of books: ${books.length}</p>

    <p>Average whimsiness level: ${averageWhimsy.toFixed(2)}</p>

    <p>Average angst level: ${averageAngst.toFixed(2)}</p>
</body>
</html>
`;
fs.writeFileSync("/data/report.html", html);
console.log("Report created :)");
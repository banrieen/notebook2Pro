$("#createWithNames").click(() => tryCatch(createWithNames));

async function createWithNames() {
  await Excel.run(async (context) => {
    const rangeToAnalyze = context.workbook.worksheets.getItem("Data Sheet").getRange("A1:E21");
    const rangeToPlacePivot = context.workbook.worksheets.getItem("Pivot Table").getRange("A2");
    context.workbook.worksheets.getItem("Pivot Table").pivotTables.add("Farm Sales", rangeToAnalyze, rangeToPlacePivot);

    await context.sync();
  });
}

//-------------------------------------------

$("#setup").click(() => tryCatch(setup));

async function setup() {
  await Excel.run(async (context) => {
    context.workbook.worksheets.getItemOrNullObject("Data Sheet").delete();
    const dataSheet = context.workbook.worksheets.add("Data Sheet");
    context.workbook.worksheets.getItemOrNullObject("Pivot Table").delete();
    const pivotSheet = context.workbook.worksheets.add("Pivot Table");

    const data = [
      ["Farm", "Type", "Classification", "Crates Sold at Farm", "Crates Sold Wholesale"],
      ["A Farms", "Lime", "Organic", 300, 2000],
      ["A Farms", "Lemon", "Organic", 250, 1800],
      ["A Farms", "Orange", "Organic", 200, 2200],
      ["B Farms", "Lime", "Conventional", 80, 1000],
      ["B Farms", "Lemon", "Conventional", 75, 1230],
      ["B Farms", "Orange", "Conventional", 25, 800],
      ["B Farms", "Orange", "Organic", 20, 500],
      ["B Farms", "Lemon", "Organic", 10, 770],
      ["B Farms", "Kiwi", "Conventional", 30, 300],
      ["B Farms", "Lime", "Organic", 50, 400],
      ["C Farms", "Apple", "Organic", 275, 220],
      ["C Farms", "Kiwi", "Organic", 200, 120],
      ["D Farms", "Apple", "Conventional", 100, 3000],
      ["D Farms", "Apple", "Organic", 80, 2800],
      ["E Farms", "Lime", "Conventional", 160, 2700],
      ["E Farms", "Orange", "Conventional", 180, 2000],
      ["E Farms", "Apple", "Conventional", 245, 2200],
      ["E Farms", "Kiwi", "Conventional", 200, 1500],
      ["F Farms", "Kiwi", "Organic", 100, 150],
      ["F Farms", "Lemon", "Conventional", 150, 270]
    ];

    const range = dataSheet.getRange("A1:E21");
    range.values = data;
    range.format.autofitColumns();

    pivotSheet.activate();

    await context.sync();
  });
}

//-------------------------------------------

$("#addRow").click(() => tryCatch(addRow));

async function addRow() {
  await Excel.run(async (context) => {
    const pivotTable = context.workbook.worksheets.getActiveWorksheet().pivotTables.getItem("Farm Sales");

    // check if the PivotTable already has rows
    const farmRow = pivotTable.rowHierarchies.getItemOrNullObject("Farm");
    const typeRow = pivotTable.rowHierarchies.getItemOrNullObject("Type");
    const classificationRow = pivotTable.rowHierarchies.getItemOrNullObject("Classification");
    pivotTable.rowHierarchies.load();
    await context.sync();

    if (typeRow.isNullObject) {
      pivotTable.rowHierarchies.add(pivotTable.hierarchies.getItem("Type"));
    } else if (farmRow.isNullObject) {
      pivotTable.rowHierarchies.add(pivotTable.hierarchies.getItem("Farm"));
    } else if (classificationRow.isNullObject) {
      pivotTable.rowHierarchies.add(pivotTable.hierarchies.getItem("Classification"));
    }

    await context.sync();
  });
}

//-------------------------------------------

$("#toggleColumn").click(() => tryCatch(toggleColumn));

async function toggleColumn() {
  await Excel.run(async (context) => {
    const pivotTable = context.workbook.worksheets.getActiveWorksheet().pivotTables.getItem("Farm Sales");

    // check if the PivotTable already has a column
    const column = pivotTable.columnHierarchies.getItemOrNullObject("Classification");
    column.load("id");
    await context.sync();

    if (column.isNullObject) {
      // adding the farm column to the column hierarchy automatically removes it from the row hierarchy
      pivotTable.columnHierarchies.add(pivotTable.hierarchies.getItem("Classification"));
    } else {
      pivotTable.columnHierarchies.remove(column);
    }

    await context.sync();
  });
}

//------------------------------------

$("#addValues").click(() => tryCatch(addValues));

async function addValues() {
  await Excel.run(async (context) => {
    const pivotTable = context.workbook.worksheets.getActiveWorksheet().pivotTables.getItem("Farm Sales");
    pivotTable.dataHierarchies.add(pivotTable.hierarchies.getItem("Crates Sold at Farm"));
    await context.sync();
  });
}

/** Default helper for invoking an action and handling errors. */
async function tryCatch(callback) {
  try {
    await callback();
  } catch (error) {
    // Note: In a production add-in, you'd want to notify the user through your add-in's UI.
    console.error(error);
  }
}

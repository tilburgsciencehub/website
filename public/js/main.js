$(".headerLink").hover(function () {
  if (!$(this).siblings().hasClass("active")) {
    $(".subMenu").removeClass("active subMenuAnimate");
  }

  if (!$(this).siblings().length) {
    $(".subMenu").removeClass("active subMenuAnimate");
  } else {
    const vm = this;

    $(this).siblings().addClass("active");
    setTimeout(function () {
      $(vm).siblings().addClass("subMenuAnimate");
    }, 100);
  }
});

$(document).mouseup(function (e) {
  const container = $(
    ".subMenu, .headerSearchResultsHolder, .buildingBlocksSuggestions"
  );

  if (!container.is(e.target) && container.has(e.target).length === 0) {
    container.removeClass("active subMenuAnimate");
  }
});

$(".headerSearch").on("keyup", function (e) {
  const resultsHolder = $(".headerSearchResultsHolder");
  const val = e.target.value;

  $.ajax({
    url: "/building-blocks/index.json",
  }).done(function (result) {
    resultsHolder.html("");
    let newResults = result.filter((result) => {
      if (new RegExp(val, "gmi").test(result.title)) {
        return result;
      }
    });

    newResults.map((result) => {
      resultsHolder.append(
        `<a class="d-block border-bottom p-3 text-secondary" href="${result.link}">${result.title}</a>`
      );
    });

    resultsHolder.addClass("active");
  });
});

$(".buildingBlockSearch").on("keyup", function (e) {
  const resultsHolder = $(".buildingBlocksSuggestions");
  const val = e.target.value;

  $.ajax({
    url: "/building-blocks/index.json",
  }).done(function (result) {
    resultsHolder.html("");
    let newResults = result.filter((result) => {
      if (new RegExp(val, "gmi").test(result.title)) {
        return result;
      }
    });

    newResults.map((result) => {
      resultsHolder.append(
        `<a class="d-block border-bottom p-3 text-secondary" href="${result.link}">${result.title}</a>`
      );
    });

    resultsHolder.addClass("active");
  });
});

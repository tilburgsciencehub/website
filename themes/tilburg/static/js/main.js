$(".headerLink").hover(function () {
  if (!$(this).hasClass("activeMenu")) {
    $(".headerLink").removeClass("activeMenu");
  }

  if (!$(this).siblings().hasClass("active")) {
    $(".subMenu").removeClass("active subMenuAnimate");
  }

  if (!$(this).siblings().length) {
    $(".subMenu").removeClass("active subMenuAnimate");
  } else {
    const vm = this;
    if (!$(this).hasClass("activeMenu")) {
      setTimeout(function () {
        $(vm).addClass("activeMenu");
      }, 300);
    }
    $(this).siblings().not(".onBoardTooltipContent").addClass("active");
    setTimeout(function () {
      $(vm).siblings().not(".onBoardTooltipContent").addClass("subMenuAnimate");
    }, 100);
  }
});

$(document).ready(function () {
  $(".pseudo-btn").on("click", function () {
    $(this).addClass("active");
    $(".TableOfContents").css("height", "auto");
    $(".TableOfContents").addClass("active");
  });

  $(".TableOfContents a").on("click", function () {
    if ($(window).width() < 992) {
      $(".pseudo-btn").removeClass("active");
      $(".TableOfContents").css("height", "56px");
      $(".TableOfContents").removeClass("active");
      setTimeout(function () {
        $(".TableOfContents").animate({ scrollTop: 0 }, "slow");
      }, 1500);
    }
  });

  $(".TableOfContents span.arrow-icon").on("click", function () {
    if ($(window).width() < 992) {
      $(".pseudo-btn").removeClass("active");
      $(".TableOfContents").css("height", "56px");
      $(".TableOfContents").removeClass("active");
    }
  });

  if ($(".sticky-top")) {
    var height = $(".sticky-top").height();
  }

  // working on codeblock
  let codeblocks = $(".codeblock");
  $(`.codeblock .downloadCodeBtn`).hide();
  for (x = 0; x < codeblocks.length; x++) {
    let blocks = $(`.codeblock:eq(${x}) .inner .highlight`);
    let d = 0;
    blocks.map((block) => {
      let title = "";
      let desc = blocks[block];
      if (
        blocks[block].children[0].children[0].className.replace(
          "language-",
          ""
        ) == "fallback"
      ) {
        title =
          blocks[block].children[0].children[0].innerHTML.match(/\-(.*?)\-/)[1];

        if (title) {
          desc = blocks[block].children[0].children[0].innerHTML.replace(
            /\-(.*?)\-/g,
            ""
          );
          blocks[block].children[0].children[0].innerHTML = desc;
        }
      } else {
        title = blocks[block].children[0].children[0].className.replace(
          "language-",
          ""
        );
      }

      $(`.codeblock:eq(${x}) .nav`).append(`
        <li class="nav-item" role="presentation">
          <a class="nav-link ${block == 0 ? "active" : ""}" id="pills-${blocks[block].children[0].children[0].className
        }-tab-${x}-${d}" data-toggle="tab" href="#${blocks[block].children[0].children[0].className
        }-${x}-${d}" role="tab" aria-controls="pills-${blocks[block].children[0].children[0].className
        }" aria-selected="true">${title}</a>
        </li>
      `);

      $(`.codeblock:eq(${x}) .tab-content`).append(`
        <div class="tab-pane ${block == 0 ? "fade show active" : ""}" id="${blocks[block].children[0].children[0].className
        }-${x}-${d}" role="tabpanel" aria-labelledby="pills-${blocks[block].children[0].children[0].className
        }-tab">
        </div>
      `);

      $(
        `.codeblock:eq(${x}) #${blocks[block].children[0].children[0].className}-${x}-${d}`
      ).append(blocks[block]);

      d++;

      var el = $(
        `.codeblock:eq(${x}) a:contains('${blocks[
          block
        ].children[0].children[0].className.replace("language-", "")}-link')`
      );

      if (el.length) {
        if ($(`.codeblock:eq(${x}) .downloadCodeBtn`).is(":hidden")) {
          $(`.codeblock:eq(${x}) .downloadCodeBtn`).show();
        }
      }

      $(`.codeblock:eq(${x}) .copyCodeBtn`).attr("data-index", x);
      $(`.codeblock:eq(${x}) .downloadCodeBtn`).attr("data-index", x);
    });
  }

  $(".share-button.copyURL").on("click", function () {
    let url = $(this).attr("data-url");
    var $temp = $('<textarea id="toCopy"></textarea>');
    $("body").append($temp);
    $temp.val(url).select();

    document.execCommand("copy");
    $temp.remove();
  });

  // make code copy-able
  $(".copyCodeBtn").on("click", function () {
    var $temp = $('<textarea id="toCopy"></textarea>');
    $("body").append($temp);
    $temp
      .val(
        $(
          `.codeblock:eq(${$(this).attr("data-index")}) .tab-pane.active code`
        ).text()
      )
      .select();

    document.execCommand("copy");
    $temp.remove();
  });

  $(".downloadCodeBtn").on("click", function () {
    var $currentlanguage = $(
      `.codeblock:eq(${$(this).attr("data-index")}) .nav-link.active`
    ).html();
    var el = $(
      `.codeblock:eq(${$(this).attr(
        "data-index"
      )}) a:contains('${$currentlanguage}-link')`
    );
    var link = el.attr("href");

    window.location.href = "../" + link;
  });

  $(".codeblock .nav-link").on("click", function () {
    var $currentlanguage = $(this).html();
    var el = $(`.codeblock a:contains('${$currentlanguage}-link')`);

    if (!el.length) {
      $(".downloadCodeBtn").hide();
    } else {
      $(".downloadCodeBtn").show();
    }
  });
});

$(document).mouseup(function (e) {
  const container = $(
    ".subMenu, .headerSearchResultsHolder, .buildingBlocksSuggestions, .headerSearchResultsHolder2"
  );

  if (!container.is(e.target) && container.has(e.target).length === 0) {
    container.removeClass("active subMenuAnimate");
    $(".headerLink").removeClass("activeMenu");
  }
});

const searchClient = algoliasearch(
  "02IYLG4AP9",
  "7009df5926509e3c685c2364242ee3f1"
);
const index = searchClient.initIndex("Tilburg_Science_Hub");

$(".headerSearch > .resetInput").on("click", function (e) {
  const value = e.target.value;
  const popularPages = fetch("/pages.json").then(res => res.json()).then(res => res)
  const resultsHolder = $(".headerSearchResultsHolder");

  resultsHolder.html(" ");
  resultsHolder.addClass("active");

  popularPages.then((results) => {
    resultsHolder.append(`<span style="font-weight: bold;">Popular Pages</span>`);
    results.map((result) => {

      resultsHolder.append(`<a href="${result.path}" style="display: flex;">
        <span style="
          display: flex;
          width: 24px;
          height: 24px;
          align-items: center;
          justify-content: center;
          border-radius: 40px;
          background-color: #003365;
          margin-right: 8px;
        "><img src="/img/arrow-trending-up.svg" width="14px" height="14px" /></span>
        <span>${result.title}</span></a>`);
    })
  })
})

// on mobile
$(".headerSearchMobile .resetInput").on("click", function (e) {
  const value = e.target.value;
  const popularPages = fetch("/pages.json").then(res => res.json()).then(res => res)
  const resultsHolder = $(".mobileResults");

  resultsHolder.html(" ");
  resultsHolder.addClass("active");

  popularPages.then((results) => {
    resultsHolder.append(`<span style="font-weight: bold;">Popular Pages</span>`);
    results.map((result) => {

      resultsHolder.append(`<a href="${result.path}" style="display: flex;">
        <span style="
          display: flex;
          width: 24px;
          height: 24px;
          align-items: center;
          justify-content: center;
          border-radius: 40px;
          background-color: #003365;
          margin-right: 8px;
        "><img src="/img/arrow-trending-up.svg" width="14px" height="14px" /></span>
        <span>${result.title}</span></a>`);
    })
  })
})

$(".headerSearch").on("keyup", function (e) {
  const resultsHolder = $(".headerSearchResultsHolder");
  const val = e.target.value;

  index
    .search(val, {
      hitsPerPage: 10,
    })
    .then(({ hits }) => {
      resultsHolder.html(" ");
      resultsHolder.addClass("active");
      hits.map((hit) => {
        let url = hit.objectID.replace("./", "");
        url = url.replace(".md", "");

        resultsHolder.append(`<a href="/${url}">${hit.title}</a>`);
      });

      if (hits.length == 0) {
        resultsHolder.append(`<span>No result found!</span>`);
      }

      // also add see more link
      if (hits.length == 10) {
        resultsHolder.append(
          `<a class="view-more-search" style="font-weight:500;border-bottom: none;" href="/search?q=${val}">View all results +</a>`
        );
      }
    });
});

$(".headerSearch2").on("keyup", function (e) {
  const resultsHolder = $(".headerSearchResultsHolder2");
  const val = e.target.value;

  index
    .search(val, {
      hitsPerPage: 10,
    })
    .then(({ hits }) => {
      resultsHolder.html(" ");
      resultsHolder.addClass("active");
      hits.map((hit) => {
        let url = hit.objectID.replace("./", "");
        url = url.replace(".md", "");

        resultsHolder.append(`<a href="/${url}">${hit.title}</a>`);
      });

      if (hits.length == 0) {
        resultsHolder.append(`<span>No result found!</span>`);
      }

      // also add see more link
      if (hits.length == 10) {
        resultsHolder.append(
          `<a class="view-more-search" style="font-weight:500;border-bottom: none;" href="/search?q=${val}">View all results +</a>`
        );
      }
    });
});

$(".headerSearchMobile").on("keyup", function (e) {
  const resultsHolder = $(".mobileResults");
  const val = e.target.value;

  index
    .search(val, {
      hitsPerPage: 10,
    })
    .then(({ hits }) => {
      resultsHolder.html(" ");
      resultsHolder.addClass("active");
      hits.map((hit) => {
        let url = hit.objectID.replace("./", "");
        url = url.replace(".md", "");

        resultsHolder.append(`<a href="/${url}">${hit.title}</a>`);
      });

      if (hits.length == 0) {
        resultsHolder.append(`<span>No result found!</span>`);
      }

      // also add see more link
      if (hits.length == 10) {
        resultsHolder.append(
          `<a class="view-more-search" style="font-weight:500;border-bottom: none;" href="/search?q=${val}">View all results +</a>`
        );
      }
    });
});

/*
 *
 * making mobile menu working
 *
 */

$(".backdrop").on("click", function () {
  $(".backdrop").addClass("d-none");
  $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").addClass("d-none");
  $(".screen-1").addClass("d-none");
  $(".screen-2").addClass("d-none");
  hideScreenTwoMenuItems();
  $("#mobileSearchMenu").addClass("d-none");
  $("#mobileCloseMenuIcon").addClass("d-none").removeClass("d-inline-block");
  $("#mobileSearchCloseMenuIcon")
    .addClass("d-none")
    .removeClass("d-inline-block");
  $("#mobileSearchIcon").removeClass("d-none");
});

$("#mobileSearchCloseMenuIcon").on("click", function () {
  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileSearchMenu").addClass("d-none");
  $(".backdrop").removeClass("active").addClass("d-none");
  $("#mobileSearchIcon").removeClass("d-none").addClass("d-inline-block");
});

$("#mobileSearchIcon").on("click", function () {
  // check if other menu is open
  if ($("#mobileBurgerIcon").hasClass("d-none")) {
    $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
    $("#mobileMenu").addClass("d-none");
    $("#mobileCloseMenuIcon").addClass("d-none").removeClass("d-inline-block");
  }

  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileSearchCloseMenuIcon")
    .removeClass("d-none")
    .addClass("d-inline-block");
  $(".backdrop").removeClass("d-none");
  setTimeout(function () {
    $(".backdrop").addClass("active");
  }, 100);
  $("#mobileSearchMenu").removeClass("d-none");
});

$("#mobileBurgerIcon").on("click", function () {
  // check if other menu is open
  if ($("#mobileSearchIcon").hasClass("d-none")) {
    $("#mobileSearchIcon").removeClass("d-none").addClass("d-inline-block");
    $("#mobileSearchMenu").addClass("d-none");
    $("#mobileSearchCloseMenuIcon")
      .addClass("d-none")
      .removeClass("d-inline-block");
  }

  $(".backdrop").removeClass("d-none");
  setTimeout(function () {
    $(".backdrop").addClass("active");
  }, 100);
  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileCloseMenuIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").removeClass("d-none");
  $(".screen-1").removeClass("d-none");
});

$("#mobileCloseMenuIcon").on("click", function () {
  $(".backdrop").removeClass("active").addClass("d-none");
  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").addClass("d-none");
  $(".screen-1").addClass("d-none");
  $(".screen-2").addClass("d-none");
});

$(".menuExpand").on("click", function () {
  if ($(this).next("div").hasClass("d-none")) {
    $(this).next("div").removeClass("d-none");
    $(this).addClass("active");
  } else {
    $(this).next("div").addClass("d-none");
    $(this).removeClass("active");
  }
});

$(".screen-1 > a").on("click", function () {
  if ($(this).attr("data-screen-two")) {
    $(".screen-1").addClass("d-none");
    $(".screen-2").removeClass("d-none");
    hideScreenTwoMenuItems();
    $(`#${$(this).attr("data-screen-two")}`).removeClass("d-none");
  }
});

function resetEverythingInMenu() {
  $("#mobileSearchIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileCloseMenuIcon").addClass("d-none").removeClass("d-none");
  $("#mobileSearchCloseMenuIcon").addClass("d-none").removeClass("d-none");
}

function hideScreenTwoMenuItems() {
  $("#mobile-building-blocks").addClass("d-none");
  $("#mobile-tutorials").addClass("d-none");
  $("#mobile-examples").addClass("d-none");
}

$(".gotoMainMenu").on("click", function () {
  $(".screen-1").removeClass("d-none");
  $(".screen-2").addClass("d-none");
});

// select pillx on hover
$(".pillx").hover(function () {
  $(".pillx").removeClass("active");
  $(this).addClass("active");

  var href = $(this).attr("href");
  $(".tab-pane").removeClass("active show");
  $(href).addClass("active show");
});

// responsive footer collapse
$("footer .footerCollapse").on("click", function () {
  $("footer .links").addClass("d-none");
  $(this).removeClass("active");
  if ($(this).children(".links").hasClass("d-block")) {
    $(this).children(".links").removeClass("d-block").addClass("d-none");
  } else {
    $(this).addClass("active");
    $(this).children(".links").addClass("d-block");
  }
});

$(".tutorialsSearch").on("keyup", function (e) {
  const resultsHolder = $(".buildingBlocksSuggestions");
  const val = e.target.value;

  $.ajax({
    url: "/tutorials/index.json",
  }).done(function (result) {
    resultsHolder.html("");
    let newResults = result.filter((result) => {
      if (new RegExp(val, "gmi").test(result.searchKeywords)) {
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
      if (new RegExp(val, "gmi").test(result.searchKeywords)) {
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

document.querySelectorAll('a[href^="#"]').forEach((trigger) => {
  trigger.onclick = function (e) {
    e.preventDefault();
    let hash = this.getAttribute("href");
    if (hash !== "#0") {
      let target = document.querySelector(hash);
      let headerOffset = 140;
      let elementPosition = target.getBoundingClientRect().top;
      let offsetPosition = elementPosition - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
    }
  };
});

if (document.querySelector("#scrollTo a")) {
  document.querySelector("#scrollTo a").click();
}

// handling wide tables
const widetables = document.querySelectorAll(".widetable");
widetables.forEach((element) => {
  element.children[0].addEventListener(
    "scroll",
    function (e) {
      if (
        element.children[0].scrollLeft + element.offsetWidth >=
        element.children[0].scrollWidth
      ) {
        element.classList.add("scrolled-right");
      } else {
        element.classList.remove("scrolled-right");
      }
    },
    false
  );
});

// onboarding tooltips
const allTooltips = $("[onBoardTooltip]");

// add all the tooltips
for (let i = 0; i < allTooltips.length; i++) {
  const div = document.createElement("div");
  div.classList.add("onBoardTooltipContent");
  div.setAttribute("current", i);

  div.innerText = allTooltips[i]?.getAttribute("onBoardTooltip");
  div.style = `left: ${allTooltips[i].getBoundingClientRect().left - 80
    }px`;

  // navigation
  const navigationDiv = document.createElement("div");
  navigationDiv.classList.add("navigation");
  navigationDiv.innerHTML = `
    <span>
      ${i == allTooltips.length - 1
      ? "&nbsp;"
      : `<a href="#0" class="skipOnboarding">Skip</a>`
    }
    </span>
    <span>
      <button type="button" class="nextButton btn btn-primary btn-sm" style="font-size: 14px; padding:  4px 12px !important;" current="${i}">${i == allTooltips.length - 1 ? "Finish" : "Next"
    } ${i + 1}/${allTooltips.length}</button>
    </span>
  `;

  div.appendChild(navigationDiv);
  $(allTooltips[i]).parent().append(div);
}

if (localStorage.getItem("demoCompleted")) {
  $(".pulse").remove();
}

$("body").on("click", ".nextButton", () => {
  const allTooltipContents = $(".onBoardTooltipContent");
  const currentActive = $(".onBoardTooltipContent.active").attr("current");

  if (allTooltipContents.length > Number(currentActive) + 1) {
    allTooltipContents[Number(currentActive)].classList.remove("active");
    allTooltipContents[Number(currentActive) + 1].classList.add("active");
  } else {
    allTooltipContents[Number(currentActive)].classList.remove("active");
    localStorage.setItem("demoCompleted", "true");
    $(".pulse").remove();
  }
});

$("body").on("click", ".skipOnboarding", () => {
  const currentActive = $(".onBoardTooltipContent.active");
  currentActive.removeClass("active");
  localStorage.setItem("demoCompleted", "true");
  $(".pulse").remove();
});

$(".takeTour").on("click", (event) => {
  $(".onBoardTooltipContent:first").addClass("active");
});

// Fill Cards Dynamically
$(document).ready(function () {
  $('.cards-home').ready(function () {
    fetch('/cards.json')
      .then(response => response.json())
      .then(data => {
        // Building Blocks
        const building_blocks = data.building_blocks || [];
        const ulElementBlock = document.getElementById('most-read-building-blocks-list');
        const buildingBlocksToDisplay = building_blocks.slice(1);

        buildingBlocksToDisplay.forEach(building_block => {
          const liElement = document.createElement('li');
          liElement.classList.add('pb-3');

          const iconElement = document.createElement('span');
          iconElement.classList.add('icon', 'link', 'text-primary', 'd-inline-block', 'mr-2');

          const linkElement = document.createElement('a');
          linkElement.href = building_block.path;

          const title = building_block.title

          linkElement.textContent = title;

          liElement.appendChild(iconElement);
          liElement.appendChild(linkElement);
          ulElementBlock.appendChild(liElement);
        });

        // Tutorials
        const tutorials = data.tutorials || [];
        const ulElementTutorial = document.getElementById('most-read-tutorials-list');
        const tutorialsToDisplay = tutorials.slice(1);

        tutorialsToDisplay.forEach(tutorial => {
          const liElement = document.createElement('li');
          liElement.classList.add('pb-3');

          const iconElement = document.createElement('span');
          iconElement.classList.add('icon', 'link', 'text-primary', 'd-inline-block', 'mr-2');

          const linkElement = document.createElement('a');
          linkElement.href = tutorial.path;

          const title = tutorial.title

          linkElement.textContent = title;

          liElement.appendChild(iconElement);
          liElement.appendChild(linkElement);
          ulElementTutorial.appendChild(liElement);
        });

        // Most Popular Building Block
        const mostPopularBuildingBlock = data.most_popular_building_block;
        const titleElementBlock = document.querySelector('#most-popular-block-single h2.heading');
        const descriptionElementBlock = document.querySelector('#most-popular-block-single p');
        const linkElementBlock = document.querySelector('#most-popular-block-single a');

        if (mostPopularBuildingBlock) {
          titleElementBlock.textContent = mostPopularBuildingBlock.title;
          descriptionElementBlock.textContent = mostPopularBuildingBlock.description;
          linkElementBlock.href = mostPopularBuildingBlock.path;
        } else {
          // If there's no most popular building block data, hide the container
          const containerElement = document.querySelector('#most-popular-block-single');
          containerElement.style.display = 'none';
        }

        // Most Popular Tutorial
        const mostPopularTutorial = data.most_popular_tutorial;
        const titleElement = document.querySelector('#most-popular-tutorial-single h2.heading');
        const descriptionElement = document.querySelector('#most-popular-tutorial-single p');
        const linkElement = document.querySelector('#most-popular-tutorial-single a');

        if (mostPopularTutorial) {
          titleElement.textContent = mostPopularTutorial.title;
          descriptionElement.textContent = mostPopularTutorial.description;
          linkElement.href = mostPopularTutorial.path;
        } else {
          // If there's no most popular tutorial data, hide the container
          const containerElement = document.querySelector('#most-popular-tutorial-single');
          containerElement.style.display = 'none';
        }

        // Code for dynamically generating carousel items
        const carouselInner = document.querySelector('.carousel-inner');

        const reproducibleData = data.categories.reproducible;

        // Iterate through the reproducible data and create carousel items
        reproducibleData.forEach(item => {
          const carouselItem = document.createElement('div');
          carouselItem.classList.add('carousel-item', 'h-100');

          if (item === reproducibleData[0]) {
            carouselItem.classList.add('active');
          }

          const carouselContent = document.createElement('div');
          carouselContent.classList.add('w-100', 'h-100');
          carouselContent.style.display = 'flex';
          carouselContent.style.alignItems = 'flex-end';

          const innerContent = document.createElement('div');

          const titleElement = document.createElement('h3');
          titleElement.classList.add('heading');
          titleElement.style.fontSize = '16px';
          titleElement.style.lineHeight = '1';
          titleElement.textContent = item.title;

          const descriptionElement = document.createElement('p');
          descriptionElement.style.fontSize = '16px';
          descriptionElement.style.color = '#6081a2';
          descriptionElement.style.fontFamily = 'acumin-pro,sans-serif';
          descriptionElement.style.width = '70%';
          descriptionElement.textContent = item.description;

          const ctaElement = document.createElement('a');
          ctaElement.textContent = 'Read more';
          ctaElement.style.setProperty('color', 'white', 'important');
          ctaElement.style.setProperty('font-family', 'forma-djr-display', 'important')
          ctaElement.href = item.path;
          ctaElement.classList.add('btn', 'btn-primary', 'my-2', 'my-sm-0', 'px-4');


          innerContent.appendChild(titleElement);
          innerContent.appendChild(descriptionElement);
          innerContent.appendChild(ctaElement);
          carouselContent.appendChild(innerContent);
          carouselItem.appendChild(carouselContent);
          carouselInner.appendChild(carouselItem);
        });


        // Code for Dynamically Setting the learn Data
        const learnData = data.categories.learn;
        const itemsRow = document.getElementById('itemsRow');

        // Iterate through the 'learn' data and create item blocks
        for (let i = 0; i < learnData.length; i += 2) {
          // Create a new row for each pair of items
          const row = document.createElement('div');
          row.classList.add('row', 'mb-3');

          // Create two item columns within the row
          for (let j = i; j < i + 2 && j < learnData.length; j++) {
            const item = learnData[j];

            // Create the item column element
            const col = document.createElement('div');
            col.classList.add('col-xl-12', 'col-lg-12', 'col-md-12', 'col-sm-12');

            // Create the item element
            const itemElement = document.createElement('div');
            itemElement.classList.add('row', 'mb-3');

            // Create the icon element
            const iconElement = document.createElement('div');
            iconElement.classList.add('icon-col', 'col-xl-4', 'col-lg-4', 'col-md-4', 'col-sm-4', 'd-flex', 'align-items-center', 'justify-content-center');
            iconElement.innerHTML = `<div class="cards-home-circle"><i class="${item.icon} fa-2xl"></i></div>`;

            // Create the content element
            const contentElement = document.createElement('div');
            contentElement.classList.add('text-col', 'col-xl-20', 'col-lg-20', 'col-md-20', 'col-sm-20');

            // Create the title and description elements
            const titleElement = document.createElement('h2');
            titleElement.classList.add('heading');
            titleElement.style.fontSize = '16px';
            titleElement.style.lineHeight = '1';
            titleElement.textContent = item.title;

            const titleLinkElement = document.createElement('a');
            titleLinkElement.href = item.path;
            titleLinkElement.style.cssText = 'color: inherit !important;';
            titleLinkElement.append(titleElement);

            const descriptionElement = document.createElement('p');
            descriptionElement.style.fontSize = '16px';
            descriptionElement.style.color = '#6081a2';
            descriptionElement.style.fontFamily = 'acumin-pro,sans-serif';
            descriptionElement.textContent = item.description;

            // Append title and description to the content element
            contentElement.appendChild(titleLinkElement);
            contentElement.appendChild(descriptionElement);

            // Append icon and content to the item element
            itemElement.appendChild(iconElement);
            itemElement.appendChild(contentElement);

            // Append the item element to the column
            col.appendChild(itemElement);

            // Append the column to the row
            row.appendChild(col);
          }

          // Append the row to the items row
          itemsRow.appendChild(row);
        }

      })
      .catch(error => console.error('Error fetching data:', error));
  });
});

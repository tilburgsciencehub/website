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

  $(".share-button.copyURL").on("click", function () {
    let url = $(this).attr("data-url");
    var $temp = $('<textarea id="toCopy"></textarea>');
    $("body").append($temp);
    $temp.val(url).select();

    document.execCommand("copy");
    $temp.remove();
  });

  // codeblocks
  $('.codeblock .nav-link').click(function (e) {
    e.preventDefault(); 

    $('.codeblock .nav-link').removeClass('active');
    $(this).addClass('active');

    $('.codeblock .highlight').addClass('highlight-inactive').removeClass('highlight-active');
    var language = $(this).data('language'); 
    $('.codeblock .highlight[data-language="' + language + '"]').removeClass('highlight-inactive').addClass('highlight-active');
  });

  // make code copy-able
  document.querySelectorAll('.copyCodeBtn').forEach(button => {
    button.addEventListener('click', function (e) {
      e.preventDefault();
      let codeBlock = this.closest('.codeblock');
      let codeContainer = codeBlock.querySelector('.highlight:not(.highlight-inactive)');
      let code = codeContainer ? codeContainer.querySelector('code') : null;
      if (code) {
        navigator.clipboard.writeText(code.textContent).then(() => {
          console.log('Code gekopieerd naar klembord!');
        }).catch(err => {
          console.error('Fout bij het kopiëren van de code: ', err);
        });
      }
    });
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
  const resultsHolder = $(".headerSearchResultsHolder");
  const mainResults = $(".mainResults");
  mainResults.html(" ");
  resultsHolder.addClass("active");
})

// on mobile
$(".headerSearchMobile .resetInput").on("click", function (e) {
  const value = e.target.value;
  const resultsHolder = $(".mobileResults");
  const mainMobileResults = $(".mainMobileResults");

  mainMobileResults.html(" ");
  resultsHolder.addClass("active");
})

function performSearch(val, resultsHolder) {
  // Controleer of de zoekterm leeg is
  if (val.trim() === "") {
    console.log("Zoekterm is leeg, zoekopdracht wordt niet uitgevoerd.");
    return; 
  }

  index
    .search(val, {
      hitsPerPage: 10,
    })
    .then(({ hits }) => {
      resultsHolder.html(" ");
      resultsHolder.addClass("active");

      const seenTitles = new Set(); // Set om unieke titels bij te houden

      hits.forEach((hit) => {
        const cleanTitle = hit.title.replace(/"/g, "");

        // Controleer of de titel al in de set zit
        if (!seenTitles.has(cleanTitle)) {
          seenTitles.add(cleanTitle); // Voeg de titel toe aan de set

          let url = hit.objectID.replace("./", "");
          url = url.replace(".md", "");
          
          resultsHolder.append(`<a href="/${url}">${cleanTitle}</a>`);
        }
      });

      if (hits.length == 0) {
        resultsHolder.append(`<span>No result found!</span>`);
      }

      if (hits.length == 10) {
        resultsHolder.append(
          `<a class="view-more-search" style="font-weight:500;border-bottom: none;" href="/search?q=${val}">View all results +</a>`
        );
      }
    });
}

function handleEventMobile(e) {
  const resultsHolder = $(".mainMobileResults");
  const val = e.target.value;
  performSearch(val, resultsHolder);
}

function handleEvent(e) {
  const resultsHolder = $(".mainResults");
  const val = e.target.value;
  performSearch(val, resultsHolder);
}

// Event listener for keyup event
$(".headerSearchMobile").on("keyup", handleEventMobile);

// Event listener for click event
$(".headerSearchMobile").on("click", handleEventMobile);

// Event listener for keyup event
$(".headerSearch").on("keyup", handleEvent);

// Event listener for click event
$(".headerSearch").on("click", handleEvent);


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
  $("#mobile-topics").addClass("d-none");
  $("#mobile-tutorials").addClass("d-none");
  $("#mobile-examples").addClass("d-none");
}

$(".gotoMainMenu").on("click", function () {
  $(".screen-1").removeClass("d-none");
  $(".screen-2").addClass("d-none");
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

document.querySelectorAll('a[href^="#"]').forEach((trigger) => {
  trigger.onclick = function (e) {
    let hash = this.getAttribute("href");
    if (hash !== "#0") {
      let target = document.querySelector(hash);
      let headerOffset = 100;
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

// Confetti Button
function animateButton(button) {
  // Reset animation
  button.classList.remove('animate');

  // Add animation class
  button.classList.add('animate');

  // Remove animation class after a delay
  setTimeout(function () {
    button.classList.remove('animate');
  }, 700);
}

// onboarding tooltips
const allTooltips = $("[onBoardTooltip]");

// add all the tooltips
for (let i = 0; i < allTooltips.length; i++) {
  const div = document.createElement("div");
  div.classList.add("onBoardTooltipContent");
  div.setAttribute("current", i);

  div.innerText = allTooltips[i]?.getAttribute("onBoardTooltip");

  if (i == allTooltips.length - 2) {
    div.style = `left: ${allTooltips[i].getBoundingClientRect().left - 20}px`;
  } else {
    div.style = `left: ${allTooltips[i].getBoundingClientRect().left - 80}px`;
  }

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
      <button type="button" class="nextButton btn btn-primary btn-sm ${i == allTooltips.length - 1 ? "confetti-button" : ""}" style="font-size: 14px; padding:  4px 12px !important;" current="${i}">
        ${i == allTooltips.length - 1
      ? "Finish"
      : "Next"
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
  var confettiButton = document.querySelector('.confetti-button');

  if (allTooltipContents.length > Number(currentActive) + 1) {
    allTooltipContents[Number(currentActive)].classList.remove("active");
    allTooltipContents[Number(currentActive) + 1].classList.add("active");
  } else {
    animateButton(confettiButton);
    setTimeout(function () {
      allTooltipContents[Number(currentActive)].classList.remove("active");
      localStorage.setItem("demoCompleted", "true");
      $(".pulse").remove();
    }, 700);
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

$(".takeTourFooter").on("click", (event) => {
  $("html, body").animate({ scrollTop: 0 }, "fast", function () {
    setTimeout(function () {
      $(".onBoardTooltipContent:first").addClass("active");
    }, 500);
  });
});

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
    $(this).siblings().addClass("active");
    setTimeout(function () {
      $(vm).siblings().addClass("subMenuAnimate");
    }, 100);
  }
});

$(document).ready(function() {
  $(".pseudo-btn").on("click", function() {
    $(this).addClass("active");
    $(".TableOfContents").css("height", "auto");
    $(".TableOfContents").addClass("active");
  });

  $(".TableOfContents a").on("click", function() {
    if ($( window ).width() < 992) {
      $(".pseudo-btn").removeClass("active")
      $(".TableOfContents").css("height", "56px");
      $(".TableOfContents").removeClass("active");
      setTimeout(function() {
        $(".TableOfContents").animate({ scrollTop: 0 }, "slow");
      }, 1500)
      
    }
    
  })

  $(".TableOfContents span.arrow-icon").on("click", function() {
    if ($( window ).width() < 992) {
      $(".pseudo-btn").removeClass("active")
      $(".TableOfContents").css("height", "56px");
    }
  })

  if ($(".sticky-top")) {
    var height = $(".sticky-top").height();
    $(".pseudoSpacer").css("height", height/1.5 + "px");
  }

  // working on codeblock
  let codeblocks = $(".codeblock")
  $(`.codeblock .downloadCodeBtn`).hide()
  for (x = 0; x < codeblocks.length; x++) {
    let blocks = $(`.codeblock:eq(${x}) .inner .highlight`)

    blocks.map(block => {
      $(`.codeblock:eq(${x}) .nav`).append(`
        <li class="nav-item" role="presentation">
          <a class="nav-link ${block == 0 ? 'active' : ''}" id="pills-${blocks[block].children[0].children[0].className}-tab-${x}" data-toggle="tab" href="#${blocks[block].children[0].children[0].className}-${x}" role="tab" aria-controls="pills-${blocks[block].children[0].children[0].className}" aria-selected="true">${blocks[block].children[0].children[0].className.replace("language-", "")}</a>
        </li>
      `);

      $(`.codeblock:eq(${x}) .tab-content`).append(`
        <div class="tab-pane ${block == 0 ? 'fade show active' : ''}" id="${blocks[block].children[0].children[0].className}-${x}" role="tabpanel" aria-labelledby="pills-${blocks[block].children[0].children[0].className}-tab">
          
        </div>
      `);

      $(`.codeblock:eq(${x}) #${blocks[block].children[0].children[0].className}-${x}`).append(blocks[block]);

      var el = $(`.codeblock:eq(${x}) a:contains('${blocks[block].children[0].children[0].className.replace("language-", "")}-link')`);

      if (el.length) {
        if ($(`.codeblock:eq(${x}) .downloadCodeBtn`).is(":hidden")) {
          $(`.codeblock:eq(${x}) .downloadCodeBtn`).show();
        }
      }

      $(`.codeblock:eq(${x}) .copyCodeBtn`).attr("data-index", x)
      $(`.codeblock:eq(${x}) .downloadCodeBtn`).attr("data-index", x)
    });
  }

  // make code copy-able
  $(".copyCodeBtn").on("click", function() {
    var $temp = $('<textarea id="toCopy"></textarea>');
    $("body").append($temp);
    $temp.val($(`.codeblock:eq(${$(this).attr("data-index")}) .tab-pane.active code`).text()).select();
    
    document.execCommand("copy");
    $temp.remove();
  })

  $(".downloadCodeBtn").on("click", function() {
    var $currentlanguage = $(`.codeblock:eq(${$(this).attr("data-index")}) .nav-link.active`).html();
    var el = $(`.codeblock:eq(${$(this).attr("data-index")}) a:contains('${$currentlanguage}-link')`);
    var link = el.attr('href');

    window.location.href = "../" + link;
  });

  $(".codeblock .nav-link").on("click", function() {
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
    ".subMenu, .headerSearchResultsHolder, .buildingBlocksSuggestions"
  );

  if (!container.is(e.target) && container.has(e.target).length === 0) {
    container.removeClass("active subMenuAnimate");
    $(".headerLink").removeClass("activeMenu");
  }
});

$(".headerSearch").on("keyup", function (e) {
  const resultsHolder = $(".headerSearchResultsHolder");
  const val = e.target.value;

  $.ajax({
    url: "/index.json",
  }).done(function (result) {
    resultsHolder.html("");
    let newResults = result.pages.filter((result) => {
      if (new RegExp(val, "gmi").test(result.searchKeywords)) {
        return result;
      }
    });

    newResults.map((result) => {
      resultsHolder.append(
        `<a class="d-block border-bottom p-3 text-secondary" href="${result.permalink}">${result.title}</a>`
      );
    });

    resultsHolder.addClass("active");
  });
});

$(".headerSearchMobile").on("keyup", function (e) {
  const resultsHolder = $(".mobileResults");
  const val = e.target.value;

  $.ajax({
    url: "/index.json",
  }).done(function (result) {
    resultsHolder.html("");
    let newResults = result.pages.filter((result) => {
      if (new RegExp(val, "gmi").test(result.searchKeywords)) {
        return result;
      }
    });

    newResults.map((result) => {
      resultsHolder.append(
        `<a class="d-block border-bottom p-3 text-secondary" href="${result.permalink}">${result.title}</a>`
      );
    });

    resultsHolder.addClass("active");
  });
});



// detect screen size change
// $(window).resize(function() {
//   if(this.resizeTO) clearTimeout(this.resizeTO);
//   this.resizeTO = setTimeout(function() {
//       location.reload();
//   }, 500);
// });

/*
 *
 * making mobile menu working
 *
 */

$(".backdrop").on("click", function() {
  $(".backdrop").addClass("d-none");
  $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").addClass("d-none");
  $(".screen-1").addClass("d-none");
  $(".screen-2").addClass("d-none");
  hideScreenTwoMenuItems()
  $("#mobileSearchMenu").addClass("d-none")
  $("#mobileCloseMenuIcon").addClass("d-none").removeClass("d-inline-block");
  $("#mobileSearchCloseMenuIcon").addClass("d-none").removeClass("d-inline-block");
  $("#mobileSearchIcon").removeClass("d-none");
});

$("#mobileSearchCloseMenuIcon").on("click", function() {
  $(this).addClass("d-none").removeClass("d-inline-block")
  $("#mobileSearchMenu").addClass("d-none")
  $(".backdrop").removeClass("active").addClass("d-none");
  $("#mobileSearchIcon").removeClass("d-none").addClass("d-inline-block");
});

$("#mobileSearchIcon").on("click", function() {

  // check if other menu is open
  if ($("#mobileBurgerIcon").hasClass("d-none")) {
    $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
    $("#mobileMenu").addClass("d-none");
    $("#mobileCloseMenuIcon").addClass("d-none").removeClass("d-inline-block")
  }

  $(this).addClass("d-none").removeClass("d-inline-block")
  $("#mobileSearchCloseMenuIcon").removeClass("d-none").addClass("d-inline-block");
  $(".backdrop").removeClass("d-none");
  setTimeout(function() {
    $(".backdrop").addClass("active");
  }, 100)
  $("#mobileSearchMenu").removeClass("d-none")
})

$("#mobileBurgerIcon").on("click", function() {

  // check if other menu is open
  if ($("#mobileSearchIcon").hasClass("d-none")) {
    $("#mobileSearchIcon").removeClass("d-none").addClass("d-inline-block");
    $("#mobileSearchMenu").addClass("d-none");
    $("#mobileSearchCloseMenuIcon").addClass("d-none").removeClass("d-inline-block")
  }

  $(".backdrop").removeClass("d-none");
  setTimeout(function() {
    $(".backdrop").addClass("active");
  }, 100)
  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileCloseMenuIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").removeClass("d-none");
  $(".screen-1").removeClass("d-none");
});

$("#mobileCloseMenuIcon").on("click", function() {
  $(".backdrop").removeClass("active").addClass("d-none");
  $(this).addClass("d-none").removeClass("d-inline-block");
  $("#mobileBurgerIcon").removeClass("d-none").addClass("d-inline-block");
  $("#mobileMenu").addClass("d-none");
  $(".screen-1").addClass("d-none");
  $(".screen-2").addClass("d-none");
});

$(".menuExpand").on("click", function() {
  if ($(this).next("div").hasClass("d-none")) {
    $(this).next("div").removeClass("d-none");
    $(this).addClass("active")
  } else {
    $(this).next("div").addClass("d-none");
    $(this).removeClass("active")
  }
  
});

$(".screen-1 > a").on("click", function() {
  if ($(this).attr("data-screen-two")) {
    $(".screen-1").addClass("d-none");
    $(".screen-2").removeClass("d-none");
    hideScreenTwoMenuItems();
    $(`#${$(this).attr("data-screen-two")}`).removeClass("d-none");
  }
})

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

$(".gotoMainMenu").on("click", function() {
  $(".screen-1").removeClass("d-none");
  $(".screen-2").addClass("d-none");
});

// select pillx on hover
$(".pillx").hover(function() {
  $(".pillx").removeClass("active");
  $(this).addClass('active')

  var href = $(this).attr("href");
  $(".tab-pane").removeClass("active show")
  $(href).addClass("active show")
  
})

// responsive footer collapse
$("footer .footerCollapse").on("click", function() {
  $("footer .links").addClass("d-none");
  $(this).removeClass("active");
  if ($(this).children(".links").hasClass("d-block")) {
    $(this).children(".links").removeClass("d-block").addClass("d-none");
  } else{
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

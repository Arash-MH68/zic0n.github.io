#!/usr/bin/env node
/**
 * Schema Markup Generator for Zic0n Engineering
 * Generates JSON-LD structured data for better SEO
 */

const schemas = {
  // Organization Schema
  organization: {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Zic0n Engineering",
    "alternateName": "Zic0n",
    "url": "https://zic0n.com",
    "logo": "https://zic0n.com/images/logo.png",
    "description": "Partner-led civil engineering practice providing geotechnical, transportation, pavements & materials, and data-enabled solutions.",
    "email": "info@zic0n.com",
    "telephone": "+1-XXX-XXX-XXXX",
    "address": [
      {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "San Diego",
        "addressRegion": "CA",
        "postalCode": "",
        "addressCountry": "US"
      },
      {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "Philadelphia",
        "addressRegion": "PA",
        "postalCode": "",
        "addressCountry": "US"
      }
    ],
    "areaServed": [
      "United States",
      "California",
      "Pennsylvania",
      "West Coast",
      "Southwest",
      "Mountain States",
      "Mid-Atlantic"
    ],
    "serviceType": [
      "Geotechnical Engineering",
      "Transportation Engineering",
      "Pavement Engineering",
      "Materials Testing",
      "Civil Engineering"
    ],
    "sameAs": [
      "https://www.linkedin.com/company/zic0n"
    ],
    "founder": [
      {
        "@type": "Person",
        "name": "Dr. Arash Hosseini",
        "jobTitle": "Co-Founder",
        "description": "Ph.D., P.E. - Geotechnical & Geo-Structural Engineering"
      },
      {
        "@type": "Person",
        "name": "Dr. Ahmed Abdalla",
        "jobTitle": "Co-Founder",
        "description": "Ph.D., P.E. - Transportation & Pavement Engineering"
      }
    ]
  },

  // FAQ Schema
  faq: {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What services does Zic0n Engineering provide?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Zic0n Engineering provides comprehensive civil engineering services including geotechnical engineering, transportation design, pavement engineering, materials testing, instrumentation, and data analytics."
        }
      },
      {
        "@type": "Question",
        "name": "Where is Zic0n Engineering located?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Zic0n Engineering is headquartered in San Diego, CA with a regional office in Philadelphia, PA. We serve clients across the United States."
        }
      },
      {
        "@type": "Question",
        "name": "What makes Zic0n Engineering different?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Zic0n is a partner-led practice co-founded by two Ph.D. P.E.s with expertise spanning geotechnical, transportation, and pavement engineering. We combine practical engineering experience with research innovation and data-driven approaches."
        }
      }
    ]
  },

  // Service Schema Template
  service: (serviceName, description) => ({
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": serviceName,
    "provider": {
      "@type": "Organization",
      "name": "Zic0n Engineering"
    },
    "description": description,
    "areaServed": "United States"
  }),

  // Breadcrumb Schema Template
  breadcrumb: (items) => ({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, index) => ({
      "@type": "ListItem",
      "position": index + 1,
      "name": item.name,
      "item": item.url
    }))
  }),

  // Local Business Schema
  localBusiness: (location) => ({
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": `Zic0n Engineering - ${location.city}`,
    "address": {
      "@type": "PostalAddress",
      "addressLocality": location.city,
      "addressRegion": location.state,
      "addressCountry": "US"
    },
    "geo": location.geo ? {
      "@type": "GeoCoordinates",
      "latitude": location.geo.lat,
      "longitude": location.geo.lng
    } : undefined,
    "url": "https://zic0n.com",
    "telephone": location.phone,
    "priceRange": "$$$$",
    "openingHours": "Mo-Fr 09:00-17:00"
  })
};

// Export for use in Node.js or browser
if (typeof module !== 'undefined' && module.exports) {
  module.exports = schemas;
}

// Make available globally in browser
if (typeof window !== 'undefined') {
  window.SchemaGenerator = schemas;
}

console.log('Schema templates generated successfully');
console.log(JSON.stringify(schemas.organization, null, 2));

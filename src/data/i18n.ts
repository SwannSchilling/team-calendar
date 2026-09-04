// Locale accessors: EN = default locale (/), DE = /de/.
// Both are dedicated builds with hand-written copy (no runtime translation).

import type { FeaturesData } from '../types';
import type { Tour } from './tour';

import * as tourEn from './tour';
import * as tourDe from './tour.de';
import featuresEn from './features.json';
import featuresDe from './features.de.json';

export type Locale = 'en' | 'de';

const tours: Record<Locale, Tour> = {
  en: tourEn as Tour,
  de: tourDe as Tour,
};

const features: Record<Locale, FeaturesData> = {
  en: featuresEn as FeaturesData,
  de: featuresDe as FeaturesData,
};

export function getTour(locale: Locale): Tour {
  return tours[locale];
}

export function getFeatures(locale: Locale): FeaturesData {
  return features[locale];
}

export type StatusKey = 'live' | 'progress' | 'pending' | 'planned' | 'verify';

export interface FeatureNote {
  key: string;
  text: string;
}

export interface Feature {
  id: number;
  title: string;
  status: StatusKey[];
  what: string;
  for: string;
  why: string;
  notes: FeatureNote[];
  differentiator: boolean;
  niche: boolean;
}

export interface Category {
  num: number;
  title: string;
  id: string;
  features: Feature[];
  plannedNote: { area: string; text: string } | null;
}

export interface Differentiator {
  title: string;
  refs: string;
  line: string;
}

export interface FeaturesData {
  compiled: string;
  categories: Category[];
  differentiators: Differentiator[];
  niche: string[];
  general: string[];
  statusCounts: Record<StatusKey, number>;
  totalFeatures: number;
}
